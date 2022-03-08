import sqlite3
connection = sqlite3.connect("Hospital.db")

getPatientid = input("Enter Patient ID to delete: ")

result = connection.execute("DELETE FROM PATIENT WHERE ID="+getPatientid)
connection.commit()
print("Deleted Successfully")
