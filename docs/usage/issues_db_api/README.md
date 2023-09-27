# Issues Database API Usage Documentation

The usage documentation for the issues database API can be viewed using an online openapi editor (i.e.
https://editor-next.swagger.io/) with the `openapi.json` file in this directory. Additionally, we have provided a high
level description of the databases in the next section, because it can be hard to grasp how all the databases fit
together.

## High level description of the databases
To get a grasp of how all the databases fit together, we will give a high level description of the databases. This could
help users or future developers of the system with changing or expanding the system.

### JiraRepos
First, we have the JiraRepos database. This is basically a read-only database, containing the issue data (e.g. summaries
and descriptions) of many issues from many repositories. It is based on [[1]](#montgomery_alternative_2022). It contains
many collections, each corresponding to a Jira repository (e.g. Apache, MongoDB, etc.). Only in case you want to update
the issue data, this database will be changed.

### MiningDesignDecisions
The next database is the MiningDesignDecisions database, containing all data related to deep learning and issue
annotation.

#### RepoInfo
The first collection is the RepoInfo collection. As explained, the JiraRepos database can be updated to refresh the
issue data. We want to keep track of things such as when we last updated a certain Jira repository. Additionally, we
also want to store some settings which are used while updating the JiraRepos database. These data and settings are all
stored in the RepoInfo collection.

#### Files
The second collection is the Files collection. This is basically a generic file storage, to store whatever the user
wants to store as plain files. These files are then stored using GridFS (note that GridFS creates two additional
collections, which are not covered in this user guide).

#### DLModels
Next, we have the DLModels collection. Each item in this collection contains a model name and config, and it contains
the versions and performances of a model. Note that the name and config are stored in plain JSON, while the versions
and performances are references to stored files in GridFS.

#### DLEmbeddings
Most models also require input embeddings. These embeddings are stored in the DLEmbeddings collection. Each item in
this collection contains a name, and it contains the config used to train the embedding. Each item can also contain a
reference to an embedding file. This embedding file is stored in GridFS.

#### IssueLabels
The IssueLabels collection's main purpose is to store all metadata related to issues. Each item in this collection
corresponds to an issue in the JiraRepos database. Each item can have an annotation (i.e. existence/property/executive).
During annotation, authors can comment on issues, which are also stored in such an item. Additionally, each issue can
have tags. Tags are used to give some extra information about issues, which can be used for sorting and ordering. For
example, you can give the tag "needs-review" for issues that should be checked by another author. Then the other author
can simply filter all issues having the tag "needs-review" and annotate such issues. Lastly, we store the predictions of
DL models for the issues that have predictions. While this is not a logical place to store the predictions, it was
needed for the Maestro UI for efficiency purposes, as MongoDB does not support efficient join operations.

#### Tags
We also have a specific collection for managing tags, i.e. the Tags collection. This collection contains all tags
currently in the database. Additionally, a tag can have a description to provide some more details about a tag. Also, a
tag has a type. Tags can be defined by users, i.e. the type is 'manual tag', but many of the tags are automatically
inserted and are of the type 'project', because they give some sort of information about the project an issue belongs
to. The exact tags we have, can be found in this collection after loading the MiningDesignDecisions database.

#### Projects
The last collection of the MiningDesignDecisions database is the Projects collection. This collection contains all
software projects that are currently in the database. Additionally, a user can insert additional properties belonging to
a certain project. All this data is stored in the Project collection.

### Users
The database API uses authentication for certain endpoints. Authentication is based on JSON web tokens, which can be
acquired by providing a correct username and password. The Users database contains the Users collection. This collection
stores the username (unique ID) and the corresponding password hash for each user. The database API uses this database
to check whether someone provided correct credentials. Hence, on a first startup, one should manually insert credentials
into this database. The following script can be used to manually insert this first user. 
After this, other users can be added using the API.

```python
import string 

from passlib.context import CryptContext
from pymongo import MongoClient

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

mongo_client = MongoClient("mongodb://localhost:27017")
users_collection = mongo_client["Users"]["Users"]

def prompt(p):
    while True:
        response = input(p)
        if not response:
            print('E: Value cannot be empty.')
            continue
        if not set(response).issubset(set(string.ascii_letters)):
            print('E: Value may only contain ascii letters and/or numbers.')
            continue
        return response  

username = prompt('Username: ')
password = prompt('Password: ')

users_collection.insert_one(
    {
        "_id": username,
        "hashed_password": pwd_context.hash(password),
    }
)
```

The script requires `passlib` and `pymongo` to be installed. These can be installed using 

```shell 
python3 -m pip install passlib[bcrypt] pymongo 
```

In case `pip` is not installed, it can be bootstrapped by running 

```shell 
curl -sS https://bootstrap.pypa.io/get-pip.py | python3
```

### Statistics
The last database is the Statistics database. This database functions as a cache for statistics of issues. For example,
it can store the description length of issues, or the amount of issues links. The exact behaviour that is desired is
flexible, and therefore this collection does not have a fixed schema.

## Importing Repos
Currently, Jira repos and their projects cannot be imported directly from the user interface.
Instead, this can be done by using the script below. Note that this script requires 
the Python requests library to be installed (`pip install requests`).

```python 
import requests


def ask(prompt, validator=None, msg=None):
    while True:
        inp = input(f'{prompt}: ')
        if not inp:
            print('E: Empty input')
        if validator is not None and not validator(inp):
            print(f'E: {msg}')
            continue
        return inp


def ask_with_default(prompt, default, validator=None, error_msg=None):
    while True:
        inp = input(f'{prompt} [default: {default}]: ')
        if not inp:
            inp = default
        if validator is not None and not validator(inp):
            print(f'E: {error_msg}')
            continue
        return inp


def authenticate(url):
    username = ask('Database Username')
    password = ask('Database Password')
    print('Retrieving login token...')
    form = (
        ('username', (None, username)),
        ('password', (None, password))
    )
    response = requests.post(f'{url}/token', files=form, verify=False)
    response.raise_for_status()
    token = response.json()['access_token']
    return token


def register():
    print('Database Credentials')
    database_url = ask('Database URL:')
    token = authenticate(database_url)
    hrule()
    print('Jira Repository')
    print('You will be asked to enter the information for a Jira repository.')
    print('Example input:')
    print('Repository name: Apache')
    print('Repository URL: https://issues.apache.org/jira')
    print()
    print('This will register the repository with the given URL under the given name in Maestro')
    print('If you later import projects from this repository, all projects will be registered as `{repo_name}-{project_name}`')
    repo_name = ask('Repository Name')
    repo_url = ask('Repository URL')
    download_date = ask_with_default('Download date (issues before this date will never be downloaded) (yyyy-mm-dd)', '1970-01-01')
    batch_size = ask_with_default('Download Batch Size (set appropriately to avoid rate limits)', 1000, str.isdigit, 'Expected an integer')
    wait_time = ask_with_default('Waiting time between batches in minutes (set appropriately to avoid rate limits)', 0, str.isdigit, 'Expected an integer')
    hrule()
    print('Registering repository...')
    payload = {
        'repo_name': repo_name,
        'repo_url': repo_url,
        'download_date': download_date,
        'batch_size': int(batch_size),
        'query_wait_time_minutes': int(wait_time)
    }
    response = requests.post(f'{database_url}/jira-repos', json=payload, headers={'Authorization': 'Bearer ' + token}, verify=False)
    response.raise_for_status()
    print('Done')


def download():
    print('Database Credentials')
    database_url = ask('Database URL:')
    token = authenticate(database_url)
    hrule()
    print('Note: if you want to download issues from repositories requiring authentication, you should download issues from them 1-by-1')
    repos = ask_with_default('What repository do you want to download issues from (comma separated list)?', 'all')
    if repos == 'all':
        repos = None
    else:
        repos = repos.split(',')
    if ask('Does this Jira Repository require authentication? [yes/no]', lambda x: x in ['yes', 'no'], 'Invalid answer') == 'y':
        username = ask('Repository Username')
        password = ask('Repository Password')
    else:
        username = password = None
    payload = {
        'repos': repos,
        'enable_auth': username is not None,
        'username': username,
        'password': password
    }
    print('Downloading issues (this may take a while)...')
    response = requests.post(f'{database_url}/jira-repos-download', json=payload, headers={'Authorization': 'Bearer ' + token}, verify=False)
    print('Done')
    


def hrule():
    print('-' * 72)



def main():
    print('Maestro -- Jira Import Utility')
    while True:
        hrule()
        option = ask('What do you want to do [register/download/exit]', lambda x: x in ('register', 'download', 'exit'), 'Invalid action')
        if option == 'register':
            register()
        if option == 'download':
            download()
        if option == 'exit':
            break
```


## References
<a id="montgomery_alternative_2022">[1]</a> Montgomery, L., Lüders, C., & Maalej, W. (2022, May). An alternative issue tracking dataset of public jira
repositories. In Proceedings of the 19th International Conference on Mining Software Repositories (pp. 73-77).