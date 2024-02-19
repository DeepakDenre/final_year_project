from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Setting import *

class MongoDB:
    def __init__(self, host, db, collection):
        self.host = host
        self.db = db
        self.collection = collection
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password), ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        self.db = self.client[self.db]
        self.collection = self.db[self.collection]

    def insert(self, data):
        self.collection.insert_one(data)

    def find(self, query):
        return self.collection.find(query)

    def find_one(self, query):
        return self.collection.find_one(query)

    def update(self, query, data):
        self.collection.update_one(query, {'$set': data})

    def delete(self, query):
        self.collection.delete_one(query)

    def delete_many(self, query):
        self.collection.delete_many(query)

    def count(self, query):
        return self.collection.count(query)

    def close(self):
        self.client.close()