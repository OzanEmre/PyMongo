from connection import ConnectionMongo
customers = ConnectionMongo("testdb", "customers").col

customer = { "name": "Ozan Emre", "address": "CastaMonica 1453"}
x = customers.insert_one(customer)
# print list of the _id values of the inserted documents:
print("Inserted: {inserted}".format(inserted = x.inserted_id))