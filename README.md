# Description
`webm_stock` is an aggregator of funny videos.

## Dev info:

### Requirements:
* Python 3.7.4 +
* Docker 19.03.4 +


### Environment:
`dev-docker-compose.yml` defines environment required for delvelopment.

`prod-docker-compose.yml` is used for production deployment.


### Actions:
**Init DEV ENV**:
``` 
docker-compose -f ./docker/dev-docker-compose.yml up -d
```
&nbsp;
**RUN prod-like env locally**:
```
docker-compose -f ./docker/prod-docker-compose.yml -p prod up -d
```
&nbsp;
**Remove prod-like env locally**:

Stop:
```
docker-compose -f ./docker/prod-docker-compose.yml -p prod stop
```

Delete containers:
```
docker-compose -f ./docker/prod-docker-compose.yml -p prod rm
```

Prune images:
```
docker image prune -a
```

**Connect to mongo**

```
docker exec -it docker_webm_db_1 /usr/bin/mongo
```
