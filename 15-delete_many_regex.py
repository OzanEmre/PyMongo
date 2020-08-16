from bson.objectid import ObjectId
from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

query = { "address": {"$regex": "^S"} }

x = customers.delete_many(query)

print(x.deleted_count, " documents deleted.")