# Maestro

A Tool to Find and Explore Architectural Design Decisions in Issue Tracking Systems

---

# Installation -- Quick Start

The components making up Maestro are divided across five separate repositories:

- [User Interface](https://github.com/mining-design-decisions/maestro-ArchUI)
- [Deep Learning Manager](https://github.com/mining-design-decisions/maestro-dl-manager)
- [Search Engine](https://github.com/mining-design-decisions/maestro-search-engine)
- [Database Setup & API](https://github.com/mining-design-decisions/maestro-issues-db)
- [Database API Wrapper Library](https://github.com/mining-design-decisions/maestro-issue-db-api-client)

The first four components are required to run the actual tool.
They can be installed by cloning each repo.

The Current repo contains the setup for Traefik and the SSL certificates. Make sure mkcert is installed. update the `install_certificates.sh` file with your IP Address. Run the shell script `install_certificates.sh` to create the SSL certificates.

The docker compose requires `maestro_traefik` network. create the maestro_treafik container using the command below

```bash
docker network create maestro_traefik
```

please update the IP of the system Afterwards, running `docker compose up --build -d` should start Traefik.

Additionally, the database API needs a secret key used for password hasing,
which can be generated using `openssl rand -hex 32`.
Afterward, the file `maestro-issues-db/issues-db-api/app/config.py` should be created,
with the following content:

```python
SECRET_KEY = '<key generated using openssl>'
```

If the database is deployed locally, the deep learning manager should be
started with the `DL_MANAGER_ALLOW_UNSAFE_SSL` environment variable set to
`true`. When running through Docker, this variable should be set in the
docker compose file, e.g. like this:

```
version: '3.1'
services:
  dl-manager:
    container_name: dl-manager
    build:
      context: ./
      dockerfile: Dockerfile-no-gpu
    image: dl-manager
    ports:
      - '9011:9011'
    environment:
      - DL_MANAGER_ALLOW_SELF_SIGNED_CERTIFICATE=TRUE
```

Next, each service can be started using docker compose. The shell script `setup_components.sh` can be used to run all the docker containers, when eachindividual componenent is installed and setup.
The following can be used as a quick-start script:

```bash
git clone https://github.com/mining-design-decisions/maestro-issues-db.git
cd maestro-issues-db
docker compose up --build -d
cd ..
git clone https://github.com/mining-design-decisions/maestro-search-engine.git
cd maestro-search-engine.git
docker compose up --build -d
cd ..
git clone https://github.com/mining-design-decisions/maestro-dl-manager.git
cd maestro-dl-manager
docker compose -f docker-compose-no-gpu.yml up --build -d
cd ..
git clone https://github.com/mining-design-decisions/maestro-ArchUI.git
cd maestro-ArchUI/flask
docker compose up --build
```

The UI can now be accessed at `https://maestro.localhost/archui`.

The deep learning manager can be start with different docker compose files in order to
enable GPU acceleration. More details can be found
[here](./docs/usage/dl_manager/index.md#running-using-docker-)

The database can be initialised with existing database archives containing
issues from many open source projects, and a number of pre-trained deep learning models.
There archives can be downloaded from [here](https://zenodo.org/record/8372644).
The JiraRepos archive contains a large number of issues from open source projects.
There are two variants of the MiningDesignDecisions archive. These archives contain
trained deep learning models. The normal variant contains a large number of different
trained models which were evaluated. The lite variant contains only the best performing
(BERT) model.
The archives can be uploaded when the database is running, by `cd`-ing into the
`maestro-issues-db` directory and executing the following commands:

JiraRepos:

```shell
docker cp ./mongodump-JiraRepos_2023-03-07-16:00.archive mongo:/mongodump-JiraRepos.archive
docker exec -i mongo mongorestore --gzip --archive=mongodump-JiraRepos.archive --nsFrom "JiraRepos.*" --nsTo "JiraRepos.*"
```

MiningDesignDecisions (normal):

```shell
docker cp ./mongodump-MiningDesignDecisions.archive mongo:/mongodump-MiningDesignDecisions.archive
docker exec -i mongo mongorestore --gzip --archive=mongodump-MiningDesignDecisions.archive --nsFrom "MiningDesignDecisions.*" --nsTo "MiningDesignDecisions.*"
```

MiningDesignDecisions (lite):

```shell
docker cp ./mongodump-MiningDesignDecisions-lite.archive mongo:/mongodump-MiningDesignDecisions-lite.archive
docker exec -i mongo mongorestore --gzip --archive=mongodump-MiningDesignDecisions-lite.archive --nsFrom "MiningDesignDecisions.*" --nsTo "MiningDesignDecisions.*"
```

By default, all data in the UI is read-only. In order to create new machine learning models or
label issues, one must be logged in.
Account creation is explained in the [usage documentation for the database API](./docs/usage/issues_db_api/README.md#users)

The URLs for the database API, keyword search API,
and the deep learning manager must be entered in the login tab of the UI.
When deploying locally, these addresses will be `https://docker.localhost/issues-db-api`, `https://docker.localhost/search-engine`,
and `https://docker.localhost/dl-manager`, respectively.
Of course, these URLs will be different when these APIs are deployed remotely.
In case of local deployment, one may have to resort to using the IP address
of the machine instead of `docker.localhost` (obtainable though `ipconfig` (windows) or `ifconfig` (unix)).
This is a limitation stemming from the fact that multiple docker compose files are used.
Fixing this issue is planned as part of future development on Maestro.

The client library is meant for the development of external scripts which interact with the database. The client library can be installed using `pip install issue-db-api`.

### Detailed Installation Instructions:

- [User Interface](./docs/usage/user_interface/README.md)
- [Deep Learning Manager](./docs/usage/dl_manager/index.md)
- [Search Engine](https://github.com/mining-design-decisions/maestro-search-engine)
- [Database Setup & API](https://github.com/mining-design-decisions/maestro-issues-db)

---

# Usage Guides

- [User Interface](./docs/usage/user_interface/index.md)
- [Deep Learning Manager](./docs/usage/dl_manager/index.md)
- [Search Engine API](./docs/usage/search_engine/README.md)
- [Database API](./docs/usage/issues_db_api/README.md)

---

# Architecture

[Click here](docs/architecture/index.md)

---

# Roadmap

Coming soon

---

# Ideas for Changes

### Refactor how testing features and features for prediction are generated

When generating features for the test set or predictions,
we need to generate the features with the same settings as the training set.
The feature generation code was designed so that by default,
it uses the configuration options which would be set when training a model.
When generating features for testing or prediction, we have to pass in a different configuration state,
and everywhere in the code, we have to check which state should be used.
This is brittle, difficult to maintain, and should be refactored.

### Make the database more scalable

Currently, some operations in the database are particularly slow.
Especially `join` operations are slow in MongoDB.
In order to speed these up, we use indexes.
However, the current database schema requires many indices,
causing the database to hit its index limit.
Either the database schema should be refactored to use fewer indices (and ideally improve performance),
or the API should be ported to use a different database (e.g. an SQL database).

### Refactor model saving

The current implementation used to store trained feature generators and models is difficult to follow and maintain.
This should be refactored to improve maintainability and make it easier to store very complex models (e.g. auto-encoders).

### Refactor deep learning input encoding handling

Currently, the deep learning code knows about four hard-coded output encodings.
Here, an output encoding is what we have been referring to as a ``deep learning task''.
For instance, we have output encoding for detection, multi-class, and multi-label.
The current implementation has all these hard-coded, including the class corresponding to each output.
We would like to change this to make it dynamically configurable.
The work required for this change would be relatively little,
but would require significant regression testing.
Making this change would be the first major step towards using the deep learning manager as a general deep learning tool,
instead of a tool specifically for training deep learning models for finding ADDs.

### Implement user-defined labels

The only labels which can be assigned to an issue are `non-archictural`,
`existence`, `executive`, and `property`.
We imagine that there are also use cases where users would want to assign other labels;
either they could want more find-grained classification,
or they could want to design classifiers for different issues
(e.g. identify issues specifically mentioning tactics).
This would require support in the user interface, deep learning manager, database, database API,
and database API client.
Doing this would also be the second (and last) change needed to convert the deep learning manager
into a general deep learning tool.

### Per-annotator labels

Currently, an issue can have only one label.
If researchers wish to compute agreement scores,
they either have to store the labels per annotators elsewhere,
or leave automatically identifiable comments containing the labels for each annotator.

### Built-in agreement calculations

Related to the per-annotator labels,
is the improvement that agreement calculations could be performed from within the UI,
instead of relying on an external script.
Currently, Maestro provides a utility script for computing inter-annotator agreement.
However, this script required annotators to leave a label in the format `label: X/Y/Z`,
where X, Y, and Z are labels.
This is not very flexible and user-friendly. Per-annotator labels would be a more user-friendly approach.

### Automatic form generation and hyperparameter optimisation in the UI

Currently, the user interface of Maestro has hard-coded pages for creating model configurations.
However, the deep learning manager has dynamic endpoints for retrieving all possible configuration
options available for models.
These endpoints could be used to dynamically generate the forms for model creation in the user interface.
This would improve the maintainability of the system because changes to the model configurations would not
require changes in the user interface.

Related to this is that the user interface has no option to perform hyperparameter optimisation.
The hyperparameter optimisation is analogous to normal model creation, except for one detail:
instead of one value, a search space of values is provided for every configuration option.
This would also be trivial to implement with dynamic form generation.

### Improve hybrid search approaches

In its current state, Maestro is mostly focused on separate keyword search and separate deep learning search.
It also has very primitive support for a hybrid search:
the results of the keyword search can be filtered based on a hard-coded deep learning classifier.
Future work could focus on making this classifier configurable,
and potentially investigating the usefulness of such configurability.
Additionally, future work could focus on implementing filtering based on multiple classifiers.

### Quality of life changes to the user interface

Some elements in the user interface (e.g. the tags associated with an issue) take up a lot of space.
This should be changed to reduce visual noise.
Additionally, inputting long queries is cumbersome with the current interface.
A general set of quality of life improvements to the user interface could greatly improve the user experience.

### Trained model deprecation policy

Trained models are currently stored in the database.
Certain changes in the deep learning manager,
such as the addition of a new parameter to a feature generator,
may cause older trained models to become unusable with the new version of Maestro.
Currently, the system does not automatically handle this.
This should be changed; there should be a system to inspect and invalidate outdated trained models.
This is currently a non-trivial change, because schema-wise,
the predictions made by these outdated models would also be deleted if these models were deleted from the database.

### Easier Installation

Currently, installing Maestro is difficult and error-prone.
We would like this to be easier. We could do this by providing
a single docker compose file, and by providing an installation script
which generates SSL certificates, starts services, and bootstraps the first user account.

### Backwards compatability in the UI

There have been many changes to the format of model configs.
Additionally, the format could change again in the future.
It would be nice if the UI were able to automatically deal with this,
by automatically detecting and updating outdated model configs.

### Improve testability

Currently, the deep learning code does not have unit tests or integration test.
The main reason for this is that it is hard to write tests for the code.
The lack of automated tests is making changes or additions to the code difficult, because they often introduce unforeseen bugs or unintended changes in behaviour.
Improving the testability of the code and writing automated tests would be a good change to make, but it certainly would require a ton of effort.

### Incremental Indexing in Search Engine

The search engine currently has to regenerate the entire index
when adding new issues or predictions. More fine-grained tracking
of when predictions are computed or when issues are updated
could potentially enable the development of partial index updates,
saving both wall and CPU time.

### Fix bugs in Search Engine

The search engine ignores the prediction filters in case there
are no predictions available for said issue.

---

# Contributing

Coming soon...
