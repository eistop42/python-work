
class Calculator:
    def __init__(self, number_1, number_2):
        """Конструктор, который выполняется при создании объекта"""
        self.number_1 = number_1
        self.number_2 = number_2
    def add(self):
        """Метод сложения"""
        return self.number_1 + self.number_2
    def subtract(self):
        """Метод вычитания"""
        return self.number_1 - self.number_2

    def divide(self):
        """Метод деления"""
        if number_2 != 0:
            return self.number_1 / self.number_2

class Logger:
    def __init__(self, filename):
        self.filename = filename

    def log_to_file(self, number_1, number_2, action):
        """Логируем строчку в файл"""
        with open(self.filename, 'a', encoding='utf-8') as f:
            log_string = f"{number_1} {number_2}: {action} \n"
            f.write(log_string)

    def read_logs(self):
        """Читаем все логи"""
        with open(self.filename, 'r', encoding='utf-8') as f:
            print(f.read())


print('Введи два числа: ')
number_1 = int(input('Первое число: '))
number_2 = int(input('Второе  число: '))

print('1 - сложить')
print('2 - вычесть')
print('3 - делить')
print('4 - прочитать логи')
ans = input('Выбери операцию: ')

# Создали экземпляры нужных классов
calculator = Calculator(number_1, number_2)

logger = Logger('logs.txt')
logger_new = Logger('logs_new.txt')


if ans == '1':
    res = calculator.add()
    print(res)
    logger.log_to_file(number_1, number_2, 'сложение')
    logger_new.log_to_file(number_1, number_2, 'сложение')
elif ans == '2':
    res = calculator.subtract()
    logger.log_to_file(number_1, number_2, 'вычитание')
    print(res)
elif ans == '3':
    res = calculator.divide()
    logger.log_to_file(number_1, number_2, 'деление')
    print(res)
elif ans == '4':
    logger.read_logs()
else:
    print('Неверная операция')