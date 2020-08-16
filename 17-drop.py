from bson.objectid import ObjectId
from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

customers.drop()