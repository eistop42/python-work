tasks = [{'name': 'поспать', 'status': 'в ожидании'}]

def add_task(name):
    """Добавление задачи"""
    task = {'name': name, 'status': 'в ожидании'}
    tasks.append(task)

def complete_task(task_number):
    """Выполнение задачи"""
    if len(tasks) >= task_number:
        task = tasks[task_number]
        task['status'] = 'Выполнена'

def show_tasks():
    """Выводим список всех задач"""
    for number, task in enumerate(tasks, 1):
        print(f"{number}. {task['name']} : {task['status']}")



while True:
    print("1 - Добавить задачу")
    print("2 - Выполнить задачу")
    print("3 - Посмотреть список задач")
    print("4 - Выйти")

    choice = input('Что ты хочешь сделать: ')

    if choice == '1':
        show_tasks()
        name = input('Название задачи: ')
        add_task(name)
        show_tasks()
    elif choice == '2':
        show_tasks()
        task_number = int(input('Введи номер задачи: '))
        task_number -= 1
        complete_task(task_number)
        show_tasks()
    elif choice == '3':
        print('Вот ваши задачи')
        show_tasks()
    elif choice == '4':
        print("До свидания!")
        break