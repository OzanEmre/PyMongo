from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

for x in customers.find():
    print(x)