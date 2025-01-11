import sqlite3

conn = sqlite3.connect("test_abc.db")

print("Opened database successfully")

c = conn.cursor()

c.execute("UPDATE students set AGE = 2 where ID = 1")

conn.commit()
conn.close()

