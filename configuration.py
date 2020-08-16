class MongoConfigurations:
    HOST = "localhost"
    PORT = "27017"
    USER = "root"
    PASSW = "example"
    def __init__(self):
        super().__init__()
        self.connstr = "mongodb://{user}:{passw}@{host}:{port}".format(host = self.HOST, port = self.PORT, user = self.USER, passw = self.PASSW)