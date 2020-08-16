from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

for x in customers.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)

print("----------------------------------")

for x in customers.find({"address": "Sideway 1633"},{ "address": 0 }):
    print(x)