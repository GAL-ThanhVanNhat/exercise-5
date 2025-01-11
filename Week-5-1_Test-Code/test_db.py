import sqlite3

conn = sqlite3.connect("test_abc.db")

print("Opened database successfully")

c = conn.cursor()

c.execute(""" DROP TABLE IF EXISTS students
            """)

c.execute(""" CREATE TABLE students(
                FIRST text,
                LAST last,
                AGE INT,
                EMAIL text,
                ID VACHAR
            )""")

print("Table created successfully")

c.execute("INSERT INTO students (FIRST, LAST, AGE, EMAIL, ID) \
    VALUES('Jean', 'Paul', 32, 'JP@HOTMAIL.COM', 1)")

c.execute("INSERT INTO students (FIRST, LAST, AGE, EMAIL, ID) \
    VALUES('Sandra', 'Allen', 25, 'SA@HOTMAIL.COM', 2)")

c.execute("INSERT INTO students (FIRST, LAST, AGE, EMAIL, ID) \
    VALUES('Salma', 'Teddy', 23, 'ST@HOTMAIL.COM', 3)")

c.execute("INSERT INTO students (FIRST, LAST, AGE, EMAIL, ID) \
    VALUES('Zack', 'Mark', 25, 'ZM@HOTMAIL.COM', 4)")

conn.commit()

print("Records created successfully")


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

