
def add(number_1, number_2):
    return number_1 + number_2
def subtract(number_1, number_2):
    return number_1 - number_2
def log_to_file(number_1, number_2, action):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        log_string = f"{number_1} {number_2}: {action} \n"
        f.write(log_string)

def read_logs():
    with open('logs.txt', 'r', encoding='utf-8') as f:
        print(f.read())

print('Введи два числа: ')
number_1 = int(input('Первое число: '))
number_2 = int(input('Второе  число: '))

print('1 - сложить')
print('2 - вычесть')
print('3 - прочитать логи')
ans = input('Выбери операцию: ')

if ans == '1':
    res = add(number_1, number_2)
    print(res)
    log_to_file(number_1, number_2, 'сложение')
elif ans == '2':
    res = subtract(number_1, number_2)
    log_to_file(number_1, number_2, 'вычитание')
    print(res)
elif ans == '3':
    read_logs()
else:
    print('Неверная операция')