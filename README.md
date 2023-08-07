# Maestro 

A Tool to Find and Explore Architectural Design Decisions in Issue Tracking Systems

---

# Installation 

The components making up Maestro are divided across five separate repositories:

- [User Interface](https://github.com/mining-design-decisions/maestro-ArchUI)
- [Deep Learning Manager](https://github.com/mining-design-decisions/maestro-dl-manager)
- [Search Engine](https://github.com/mining-design-decisions/maestro-search-engine)
- [Database Setup & API](https://github.com/mining-design-decisions/maestro-issues-db)
- [Database API Wrapper Library](https://github.com/mining-design-decisions/maestro-issue-db-api-client)

The first four components are required to run the actual tool. They can be installed by cloning the repos and starting the services by running 

```bash 
docker compose up --build -d 
```

The UI can now be accesed at `http://localhost:5000`.

The client library is meant for the development of external scripts which interact with the database. The client library can be installed using `pip install issue-db-api`.

---

# Architecture 

[Click here](docs/architecture/index.md) 

---

# Roadmap 

Coming soon

--- 

# Contributing 

Coming soon...
