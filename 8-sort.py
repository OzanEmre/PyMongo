from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col
doc = customers.find().sort("name")
for x in doc:
    print(x)

print("----------------------------------")

doc = customers.find().sort("name", -1)
for x in doc:
  print(x)