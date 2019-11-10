ENV

Mongo:
docker run --name webm_mongodb -p 27017:27017 -d mongo:4.2 

Connect:
docker exec -it webm_mongodb /bin/bash

### Docker compose

#### Start:
docker-compose -p 'webm_stock' up -d

#### Stop:
docker-compose -p 'webm_stock' stop

---


## Setup Python(min 3.6) environment

1. init new virtual env
```
python3 -m venv env
```
2. activate it
```
source env/bin/activate
```
3. install dependencies
```
pip install -r requirements.txt
``` 

### Actions:
Add dependency:
```
pip install <packade_name>
```
and then update `requirements.txt`
```
pip freeze > requirements.txt
```

Deactivate virtual env:
```
deactivate
```