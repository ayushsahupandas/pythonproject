import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO students (name, age) VALUES ('Ravi', 21)")
    conn.commit()
    print("Transaction committed.")
except:
    conn.rollback()
    print("Transaction rolled back.")

conn.close()
