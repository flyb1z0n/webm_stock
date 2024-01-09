## Connect to mongo

```
docker exec -it docker_webm_db_1 /usr/bin/mongo
use webm_stock
```


## Find file by ID
```
db.files.find( { _id: ObjectId("5eb2b3ccc72fcaf905ffb8d4")} )
```

## Remove file by ID
```
db.files.remove( { _id: ObjectId("5eb2b3bcc72fcaf905ffb8c0")} )
```

## Find files older than
```
db.files.find({ creation_date: { $lt: new Date('2020-11-01') }})
```

## Remove files older than
```
db.files.remove({ creation_date: { $lt: new Date('2020-11-01') }})
```

## Remove threads older than
```
db.threads.remove({ creation_date: { $lt: new Date('2020-11-01') }})
```