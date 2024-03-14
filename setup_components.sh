#!/bin/sh
docker compose -f docker-compose.yml up --build -d
docker compose -f ../maestro-issues-db/docker-compose.yml up --build -d
docker compose -f ../maestro-ArchUI/docker-compose.yml up --build -d
docker compose -f ../maestro-search-engine/docker-compose.yml up --build -d
