from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

query = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

customers.update_one(query, newvalues)

for x in customers.find():
  print(x)