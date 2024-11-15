import sqlite3

def get_tasks():
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute('select * from task')
    rows = cursor.fetchall()
    connection.close()
    return rows


def add_task(name):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute('insert into task (name, status) values (?,?)', (name, 'сделать'))
    connection.commit()
    connection.close()

def delete_task(task_id):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute('delete from task where id = ? ', (task_id, ))
    connection.commit()
    connection.close()


def update_task(task_id):
    connection = sqlite3.connect('todo.db')
    cursor = connection.cursor()
    cursor.execute("update task set status = 'сделано' where id=?", (task_id, ))
    connection.commit()
    connection.close()


emoji = {'сделать': '🔵', 'сделано': '🟢'}


while True:
    print('Что хотите сделать?')
    print('1 - прочитать задачи')
    print('2 - добавить задачу')
    print('3 - удалить задачу')
    print('4 - выполнить задачу')

    res = input('Вводи номер: ')
    if res == '1':
        rows = get_tasks()
        print('\n Вот список задач')
        for row in rows:
            task_string = f'{row[0]}. {row[1]} - {row[2]}{emoji[row[2]]}'
            print(task_string)
        print('\n')
    elif res == '2':
        name = input('Введи название задачи: ')
        add_task(name)
        print('Задача добавлена!')
    elif res == '3':
        task_id = input('Введи id задачи: ')
        delete_task(task_id)
        print('Задача удалена 😎!')
    elif res == '4':
        task_id = input('Введи id задачи: ')
        update_task(task_id)
        print('Задача выполнена 😎!')
    if res == 'q':
        break
