import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students (name, major, score);")

students = [
    {"name": "Amirali", "major": "Computer Engineering", "score": "16.50"},
    {"name": "Sepide", "major": "Civil Engineering", "score": "18.15"},
    {"name": "Sahand", "major": "Biomedical Engineering", "score": "17.00"},
    {"name": "Kian", "major": "Data Science", "score": "14.50"},
]

# for person in students:
#     command = f"INSERT INTO students VALUES {(person['name'],person['major'],person['score'])};"
#     cur.execute(command)

cur.execute("SELECT * FROM students;")
records = cur.fetchall()

for i in records:
    if float(i[-1]) >= 17:
        print(i)

con.commit()
con.close()
print("Done")

# ------------------------------------------------------------------------------------------------------

# import sqlite3
#
# con = sqlite3.connect('info.db')
# cur = con.cursor()
#
# # cur.execute("CREATE TABLE IF NOT EXISTS students (name, major, score);")
#
# # cur.execute("INSERT INTO students VALUES ('Mohsen','Computer Engineering','17.00');")
# # cur.execute("INSERT INTO students VALUES ('Mina','Civil Engineering','18.15');")
# # cur.execute("INSERT INTO students VALUES ('Kian','Data Science','16.50');")
# # cur.execute("INSERT INTO students VALUES ('Hasti','Biomedical Engineering','14.50');")
#
# cur.execute("SELECT * FROM students WHERE score >= '17';")
# records = cur.fetchall()
#
# for i in records:
#     print(i)
#
# con.commit()
# con.close()
# print("Done")
