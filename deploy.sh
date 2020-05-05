#!/bin/sh
git pull

docker-compose -f ./docker/prod-docker-compose.yml build
docker-compose -f ./docker/prod-docker-compose.yml stop
docker-compose -f ./docker/prod-docker-compose.yml up -d