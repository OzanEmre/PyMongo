from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

query = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = customers.update_many(query, newvalues)

print(x.modified_count, "documents updated.")

for x in customers.find():
  print(x)