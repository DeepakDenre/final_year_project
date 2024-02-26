from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
from Setting import *

class MongoDB:
    def __init__(self, host, db, attendance, student):
        notWorking = True
        while notWorking:
            try:
                self.driver1 = MongoClient(host % (username, password), server_api=ServerApi('1'))
                self.driver2 = MongoClient(host % (username, password), server_api=ServerApi('1'))
                notWorking = False
            except Exception as e:
                pass
        try:
            self.driver1.admin.command('ping')
            print("You successfully connected to MongoDB! on %s database and collection %s" % (db,attendance))
            self.driver2.admin.command('ping')
            print("You successfully connected to MongoDB! on %s databaseand collection %s" % (db,student))
        except Exception as e:
            print(e)
        self.db1 = self.driver1[db]
        self.db2 = self.driver2[db]
        self.Attendance = self.db1[attendance]
        self.student = self.db2[student]
    
    def addAttendance(self, card):
        try:
            dateArrary = (self.Attendance.find_one({"card": card}))["date"]
            if datetime.today().strftime("%d-%m-%Y") not in dateArrary:
                dateArrary.append(datetime.today().strftime("%d-%m-%Y"))
                self.Attendance.update_one({"card": card}, {"$set": {"name": self.getName(card),"card": card, "date": dateArrary}}, upsert=True)
                return True
            else:
                return False
        except:
            self.Attendance.insert_one({"name": self.getName(card),"card": card, "date": [datetime.today().strftime("%d-%m-%Y")]})
            return True

    def validateCard(self, card):
        if self.student.find_one({"card": card}) == None:
            return False
        else:
            return True

    def getName(self, card):
        return self.student.find_one({"card": card})["name"]
    