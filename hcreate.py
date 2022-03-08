# import sqlite3
# connection = sqlite3.connect("hospital.db")

# connection.execute('''CREATE TABLE PATIENT(
#                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                     PATIENT_ID INTEGER,
#                     PATIENT_NAME TEXT,
#                     ADDRESS TEXT,
#                     PHONE_NUMBER INTEGER,
#                     EMAIL TEXT,
#                     PINCODE INTEGER
# )''')

print("Table Created Successfully ")

getPid = input("Enter Patient ID: ")
getPname = input("Enter Patient Name: ")
getAddress = input("Enter Address: ")
getPhonenu = input("Enter Phone Number: ")
getEmail = input("Enter Email: ")
getPincode = input("Enter Pincode: ")


connection.execute(" INSERT INTO PATIENT(PATIENT_ID, PATIENT_NAME, ADDRESS, PHONE_NUMBER, EMAIL, PINCODE) \
 VALUES("+getPid+",'"+getPname+"','"+getAddress+"',"+getPhonenu+",'"+getEmail+"',"+getPincode+")")
connection.commit()
connection.close()
print("Inserted Successfully")