import sqlite3

connection = sqlite3.connect("Hospital.db")
connection.execute(''' CREATE TABLE IF NOT EXISTS DOCTORS(
                NAME TEXT,
                EMAIL_ID TEXT,
                QUALIFICATION TEXT,
                ADDRESS TEXT,
                PHONENO TEXT
);''')

print("Table Created Successfully")