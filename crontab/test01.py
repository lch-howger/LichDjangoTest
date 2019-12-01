import os
import sqlite3

sql_create_table = 'CREATE TABLE stars (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, star TEXT NOT NULL, time TEXT NOT NULL, text TEXT NOT NULL)'

# connect to the database from filename
file_exists = os.path.exists('./stars.db')
if file_exists:
    os.remove('./stars.db')

# connect to the database and get the cursor
db = sqlite3.connect('./stars.db')
cursor = db.cursor()

# create database and table
cursor.execute(sql_create_table)
db.commit()
cursor.close()
