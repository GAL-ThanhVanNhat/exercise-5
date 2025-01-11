import sqlite3

conn = sqlite3.connect("test_abc.db")

print("Opened database successfully")

c = conn.cursor()

c.execute("DELETE from students where ID = 1")

conn.commit()
conn.close()