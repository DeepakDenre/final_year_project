from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from Setting import *

class MongoDB:
    def __init__(self, host, db, collection):
        self.db = db
        self.collection = collection
        self.client = MongoClient(host % (username, password), server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("You successfully connected to MongoDB! on %s database and %s collection" % (db, collection))
        except Exception as e:
            print(e)
        self.db = self.client[self.db]
        self.collection = self.db[self.collection]

    def attendanceMark(self,card):
        details=self.collection.insert_one({"Card": card})