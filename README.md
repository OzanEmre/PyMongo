## PyMongo Tutorial (Python 3.8.1)

Docker command
#docker run -d --publish 27017:27017 --restart always --name mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=example mongo
#docker run -d --link mongo:mongo --restart always --publish 8081:8081 --name mongo-express -e ME_CONFIG_MONGODB_ADMINUSERNAME=root -e ME_CONFIG_MONGODB_ADMINPASSWORD=example mongo-express

Mongo bash on docker
> docker exec -it mongo bash //linuxta sonraki komut satırında: mongo
-- mongo "mongodb://root:example@localhost:27017/admin" //linux
 use testDb //create/select db
 db.createCollection("TestData") //create collection
 db.TestData.insert({isInsert:true}) //insert data in collection
 
 db.auth("root","example")
 
 db.createUser({user: "testuser", pwd: "qwert1234", roles:[{ role: "read", db: "testdb" }, { role: "readWrite", db: "testdb" }]})
 db.auth("testuser","qwert1234")

Sources: https://api.mongodb.com/python/current/tutorial.html
https://medium.com/@MicroPyramid/mongodb-crud-operations-with-python-pymongo-a26883af4d09
https://www.w3schools.com/python/python_mongodb_getstarted.asp
