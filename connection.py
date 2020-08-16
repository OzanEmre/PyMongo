import pymongo
from configuration import MongoConfigurations

class ConnectionMongo:
    def __init__(self, database, collection):
        super().__init__()
        config = MongoConfigurations()

        self.client = pymongo.MongoClient(config.connstr)
        self.db = self.client[database]
        self.col = self.db[collection]