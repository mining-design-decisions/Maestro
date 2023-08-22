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

The deep learning manager, search engine, and database API all need SSL certificates
to function: 

- For the deep learning, the full details can be found in the 
[usage guide](./docs/usage/dl_manager/index.md#preparations-before-running-).
When running the deep learning manager using docker compose, the key file must be 
called `server.key` and the certificate file must be called `server.crt`.
These files must be contained in the same file as the `Dockerfile` file, 
which is simply the `maestro-dl-manager` folder.

- The keyword search engine requires specific names for the certificate and key files.
They should be called `fullchain.pem` and `privkey.pem`, respectively. 
Both files should be contained in the same folder as the `Dockerfile` file, which 
is the `maestro-search-engine/pylucene` folder.

- The certificate and key files for the database API can have arbitrary names.
The files should both be placed in the same file as the `Dockerfile` file,
which is the `maestro-issues-db/issues-db-api` folder.
Additionally, the database API needs a secret key used for password hasing,
which can be generated using `openssl rand -hex 32`.
Afterward, the file `maestro-issues-db/issues-db-api/app/config.py` should be created,
with the following content:
```python
SECRET_KEY = '<key generated using openssl>'
SSL_KEYFILE = '<name of key file>'
SSL_CERTFILE = '<name of certificate file>'
```

Note that every service can have its own SSL certificate; they do not all need to use the same one. 

In case of local deployment (and **only** in case of local deployment), self-signed
SSL certificates can be used. The following command can be used to generate 
self-signed certificates using OpenSSL (note: all fields in the prompt can be left blank):

```shell 
openssl req -new -x509 -nodes -sha256 -out server.crt -keyout server.key
```

Windows users can use the Bash shell installed alongside 
[Git for Windows](https://gitforwindows.org/) in order to get access to the openssl command.

Next, each service can be started using docker compose.
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

The UI can now be accessed at `http://localhost:5000`.

The deep learning manager can be start with different docker compose files in order to 
enable GPU acceleration. More details can be found 
[here](./docs/usage/dl_manager/index.md#running-using-docker-)

The URLs for the database API, keyword search API,
and the deep learning manager must be entered in the login tab of the UI. 
When deploying locally, these addresses will be `https://localhost:8000`, `https://localhost:8042`,
and `https://localhost:9011`, respectively. 
Of course, these URLs will be different when these APIs are deployed remotely.

By default, all data in the UI is read-only. In order to create new machine learning models or 
label issues, one must be logged in.
Account creation is explained in the [usage documentation for the database API](./docs/usage/issues_db_api/README.md#users)

The client library is meant for the development of external scripts which interact with the database. The client library can be installed using `pip install issue-db-api`.

### Detailed Installation Instructions:

- [User Interface](./docs/usage/user_interface/README.md)
- [Deep Learning Manager](./docs/usage/dl_manager/index.md)
- [Search Engine](https://github.com/mining-design-decisions/maestro-search-engine)
- [Database Setup & API](https://github.com/mining-design-decisions/maestro-issues-db)

---

# Usage Guides 

- [User Interface](./docs/usage/user_interface/README.md)
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

# Contributing 

Coming soon...
