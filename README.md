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
They can be installed by cloning each repo and starting each service using docker compose.
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

By default, all data in the UI is read-only. In order to create new machine learning models or 
label issues, one must be logged in.
Account creation is explained in the [usage documentation for the database API](./docs/usage/issues_db_api/README.md#users)

The client library is meant for the development of external scripts which interact with the database. The client library can be installed using `pip install issue-db-api`.

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
