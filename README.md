ENV

Mongo:
docker run --name webm_mongodb -p 27017:27017 -d mongo:4.2 

Connect:
docker exec -it webm_mongodb /bin/bash