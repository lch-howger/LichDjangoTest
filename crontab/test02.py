import sqlite3

sql_insert_task = "INSERT INTO stars VALUES(NULL,'{}','{}','{}')"

db = sqlite3.connect('./stars.db')
cursor = db.cursor()
cursor.execute(sql_insert_task.format('abc', 'abc', 'abc'))
db.commit()
cursor.close()