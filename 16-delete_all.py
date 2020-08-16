from bson.objectid import ObjectId
from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

x = customers.delete_many({})

print(x.deleted_count, " documents deleted.")