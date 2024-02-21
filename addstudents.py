import MongoDB
from Setting import *

db = MongoDB.MongoDB(dbHost, "Attendance", "students")

name = input("Enter the name of the student: ")
card = input("Enter the card number: ")
roll = input("Enter the roll number: ")
class_id = input("Enter the class: ")

db.collection.insert_one(
    {
    "Name": name,
    "Card": card,
    "Roll": roll,
    "Class": class_id
    }
)
