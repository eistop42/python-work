import sqlite3

connection = sqlite3.connect('students')

cursor = connection.cursor()

cursor.execute('select * from student')
rows = cursor.fetchall()
# print(rows)
#
# for row in rows:
#     print(row[1], row[2])
#


cursor.execute("insert into student (fio, email, class_id) values ('Марина Е', 'dfad', 1);")

student = ['Николай', 'sdf@sdf.ru', '2']
cursor.execute("insert into student (fio, email, class_id) values (?, ?, ?);", (student[0], student[1], student[2]))


connection.commit()

connection.close()

