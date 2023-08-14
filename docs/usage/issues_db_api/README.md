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
into this database.

### Statistics
The last database is the Statistics database. This database functions as a cache for statistics of issues. For example,
it can store the description length of issues, or the amount of issues links. The exact behaviour that is desired is
flexible, and therefore this collection does not have a fixed schema.

## References
<a id="montgomery_alternative_2022">[1]</a> Montgomery, L., Lüders, C., & Maalej, W. (2022, May). An alternative issue tracking dataset of public jira
repositories. In Proceedings of the 19th International Conference on Mining Software Repositories (pp. 73-77).