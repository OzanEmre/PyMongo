from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

query = {"address": "Sideway 1633"}

for x in customers.find(query):
    print(x)

print("----------------------------------")

query = { "address": { "$gt": "S" } }
doc = customers.find(query)
for x in doc:
  print(x)

print("----------------------------------")

query = { "address": { "$regex": "^M" } }
doc = customers.find(query)
for x in doc:
  print(x)