import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Insert
cursor.execute("INSERT INTO students (name, age) VALUES ('Ayush', 19)")

# Update
cursor.execute("UPDATE students SET age = 20 WHERE name = 'Ayush'")

# Select
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Delete
cursor.execute("DELETE FROM students WHERE name = 'Ayush'")

conn.commit()
conn.close()
