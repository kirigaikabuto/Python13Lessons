# pip install pymongo
import pymongo


class Mongo:
    def __init__(self, database_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def list(self):
        data = self.collection.find()
        return list(data)

    def create(self, document):
        self.collection.insert(document)
