# Development:

## Requirements:
* Python 3.7.4 +
* Docker 19.03.4 +

&nbsp;

## Start application
* **Rest API:**
```
python -m rest
```

## Python:

1. init new virtual env
```
python3 -m venv api_env
```
2. activate it
```
source api_env/bin/activate
```
3. install dependencies
```
pip install -r requirements.txt
``` 
&nbsp;
### Actions:
* **Add dependency:**
```
pip install <packade_name>
```
and then update `requirements.txt`
```
pip freeze > requirements.txt
```
&nbsp;
* **Deactivate virtual env:**
```
deactivate
```

## Environment:
`dev-docker-compose.yml` defines environment required for delvelopment.

`prod-docker-compose.yml` is used for production deployment.


### Actions:
* **Init DEV ENV**:
``` 
docker-compose -f ./docker/dev-docker-compose.yml up -d
```
&nbsp;
* **RUN prod-like env locally**:
```
docker-compose -f ./docker/prod-docker-compose.yml -p prod up -d
```
&nbsp;
* **Remove prod-like env locally**:

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


&nbsp;
* **Connect to mongo**

```
docker exec -it docker_webm_db_1 /usr/bin/mongo
```
