from bson.objectid import ObjectId
from connection import ConnectionMongo
database = ConnectionMongo("testdb", "customers").db

dblist = database.list_collection_names()
print(dblist)

if "customers" in dblist:
  print("Collection exists.")
else:
    print("Collection not exists")
