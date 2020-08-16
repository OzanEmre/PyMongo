from connection import ConnectionMongo
customers = ConnectionMongo("mydatabase", "customers").col

doc = customers.find().limit(5)

for x in doc:
  print(x)

print("----------------------------------")

doc = customers.find().limit(11).sort("_id", -1)

for x in doc:
  print(x)