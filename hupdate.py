import sqlite3

connection = sqlite3.connect("Hospital.db")

getPatientid = input("Enter Patient ID to change: ")

getNpid = input("Enter New Patient ID: ")
getNpname = input("Enter New Patient Name: ")
getNaddress = input("Enter New Address: ")
getNphonenu = input("Enter New Phone Number: ")
getNemail = input("Enter New Email: ")
getNpincode = input("Enter New Pincode: ")

result = connection.execute(" UPDATE PATIENT SET PATIENT_ID="+getNpid+", PATIENT_NAME='"+getNpname+"', \
ADDRESS='"+getNaddress+"', PHONE_NUMBER="+getNphonenu+", EMAIL='"+getNemail+"', PINCODE="+getNpincode+" WHERE PATIENT_ID="+getPatientid)
connection.commit()
print("Updated Successfully")