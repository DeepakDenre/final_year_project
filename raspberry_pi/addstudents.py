import MongoDB
from Setting import *
import NFC

db = MongoDB.MongoDB(dbHost, "Attendance","attendance","student")

name = input("Enter the name of the student: ")
print("Scan the card number: ")
card = NFC.NFC().uidListToStr(NFC.NFC().readCard())
roll = input("Enter the roll number: ")
class_id = input("Enter the class: ")

try:
    db.student.insert_one(
        {
            "name": name,
            "card": card,
            "roll": roll,
            "class": class_id  
        }
    )
    print("Student added successfully")
except Exception as e:
    print(e)
    print("Error in adding the student")