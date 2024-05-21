#!/bin/sh
# Check if the network maestro_traefik exists
if ! docker network inspect maestro_traefik >/dev/null 2>&1; then
    echo "Creating maestro_traefik network..."
    docker network create maestro_traefik
else
    echo "maestro_traefik network already exists, skipping creation..."
fi
docker compose -f docker-compose.yml up --build -d
docker compose -f ../maestro-issues-db/docker-compose.yml up --build -d
docker compose -f ../maestro-ArchUI/docker-compose.yml up --build -d
docker compose -f ../maestro-search-engine/docker-compose.yml up --build -d
