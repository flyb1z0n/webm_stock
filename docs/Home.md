## Dev info:

### Requirements:
* Python 3.7.4 +
* Docker 19.03.4 +


### Environment:
`dev-docker-compose.yml` defines environment required for delvelopment.

`prod-docker-compose.yml` is used for production deployment.

### Virtual environment configuration

1. init new virtual env
```
python3 -m venv _venv
```
2. activate it
```
source _venv/bin/activate
```
3. install dependencies
```
pip install -r requirements.txt
``` 

## Start application
* **Start Crawler:**
```
python -m crawler
```

* **Rest API:**
```
python -m api
```

### Actions:
* **Add dependency:**
```
pip install <packade_name>
```
and then update `requirements.txt`
```
pip freeze > requirements.txt
```


**Init DEV ENV**:
``` 
docker-compose -f ./_docker/dev-docker-compose.yml up -d
```
&nbsp;
**Build**:
```
docker-compose -f ./_docker/prod-docker-compose.yml -p prod build
```

**RUN prod-like env locally**:
&nbsp;
```
docker-compose -f ./_docker/prod-docker-compose.yml -p prod up -d
```
&nbsp;
**Remove prod-like env locally**:

Stop:
```
docker-compose -f ./_docker/prod-docker-compose.yml -p prod stop
```

Delete containers:
```
docker-compose -f ./_docker/prod-docker-compose.yml -p prod rm
```

Prune images:
```
docker image prune -a
```

**Connect to mongo**

```
docker exec -it docker_webm_db_1 /usr/bin/mongo
```

&nbsp;
**Useful links for Developers:**

* [Flask documentation](https://flask.palletsprojects.com/)
* [Flask-restx documentation](https://flask-restx.readthedocs.io/en/latest/)