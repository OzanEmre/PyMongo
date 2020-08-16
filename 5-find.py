from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

x = customers.find_one()

print(x)