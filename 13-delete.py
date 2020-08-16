from bson.objectid import ObjectId
from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

documentId = "5e1a4526d65c8b907daac8a5"

result = customers.delete_one({"_id": ObjectId(documentId)})