import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def get_tasks(self, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('select * from task where user_id = ?', (user_id, ))
            rows = cursor.fetchall()
            return rows

    def add_task(self, name, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute('insert into task (name, status, user_id) values (?,?,?)', (name, 'сделать', user_id))

    def delete_task(self, task_id, user_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            res = cursor.execute('delete from task where id = ? and user_id = ?', (task_id, user_id))
            print(res.fetchall())
    def update_task(self, task_id):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            cursor.execute("update task set status = 'сделано' where id=?", (task_id,))


emoji = {'сделать': '🔵', 'сделано': '🟢'}


db = Database('C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\todo.db')


name = input('Введи имя: ')
password = input('Введи пароль: ')

db_name = 'C:\\Users\\Б - Преподаватель\\Documents\\Евдокимов Илья\\python-work\\db\\todo.db'

auth = False
with sqlite3.connect(db_name) as connection:
    cursor = connection.cursor()
    rows = cursor.execute("select * from user where name = ? and password = ? ", (name, password))
    res = rows.fetchone()

    if res:
        auth = True
        user_id = res[0]
        print('Авторизация успешна')
    else:
        print('неверный логин или пароль')


while True and auth:
    print('Что хотите сделать?')
    print('1 - прочитать задачи')
    print('2 - добавить задачу')
    print('3 - удалить задачу')
    print('4 - выполнить задачу')

    res = input('Вводи номер: ')
    if res == '1':
        rows = db.get_tasks(user_id)
        print('\n Вот список задач')
        for row in rows:
            task_string = f'{row[0]}. {row[1]} - {row[2]}{emoji[row[2]]}'
            print(task_string)
        print('\n')
    elif res == '2':
        name = input('Введи название задачи: ')
        db.add_task(name, user_id)
        print('Задача добавлена!')
    elif res == '3':
        task_id = input('Введи id задачи: ')
        db.delete_task(task_id, user_id)
        print('Задача удалена 😎!')
    elif res == '4':
        task_id = input('Введи id задачи: ')
        db.update_task(task_id)
        print('Задача выполнена 😎!')
    if res == 'q':
        break
