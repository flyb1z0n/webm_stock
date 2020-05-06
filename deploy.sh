#!/bin/sh
git pull

cd _docker
docker-compose -f ./prod-docker-compose.yml build
docker-compose -f ./prod-docker-compose.yml stop
docker-compose -f ./prod-docker-compose.yml up -d