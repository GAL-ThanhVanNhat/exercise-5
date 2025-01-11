import sqlite3

conn = sqlite3.connect("test_abc.db")

print("Opened database successfully")

c = conn.cursor()

cursor = conn.execute("SELECT FIRST, LAST, AGE, EMAIL, ID from students")

for row in cursor:
    print("FIRST = ", row[0])
    print("LAST = ", row[1])
    print("AGE = ", row[2])
    print("EMAIL = ", row[3])
    print("ID = ", row[4]), "\n" 
    
print("Operation done successfully")

conn.commit()
conn.close()
