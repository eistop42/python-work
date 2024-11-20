import sqlite3

connection = sqlite3.connect('C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\todo.db')

cursor = connection.cursor()

cursor.execute('Select * from bank')
cursor.execute('update bank set money = money + 500 where name="миша"')
connection.commit()
cursor.execute('update bank set money = money - 500 where name="антон"')

connection.commit()
connection.close()