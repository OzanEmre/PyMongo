from bson.objectid import ObjectId
from connection import ConnectionMongo
client = ConnectionMongo("testdb", "customers").client

dblist = client.list_database_names()
print(dblist)

if "mydatabase" in dblist:
  print("The database exists.")
else:
    print("Database not exists")
