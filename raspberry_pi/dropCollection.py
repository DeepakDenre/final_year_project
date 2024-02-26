import MongoDB
from Setting import *

driver = MongoDB.MongoDB(dbHost, "Attendance", "attendance", "student")

try:
    print("Collections present in the database: ")
    print(driver.db1.list_collection_names())
    choice = int(input("Which collection do you want to drop? : "))
    driver.db1.drop_collection(driver.db1.list_collection_names()[choice+1])
    print("Collections dropped successfully")

except Exception as e:
    print(e)