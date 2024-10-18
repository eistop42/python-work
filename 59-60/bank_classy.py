class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, money):
        if money < 0:
            raise ValueError('Некорректная сумма')
        self.balance += money
        print(f'Положил {money}')

    def withdraw(self, money):
        if money < 0:
            raise ValueError('Некорректная сумма')
        if money > self.balance:
            raise ValueError('У вас нет столько денег :(')
        self.balance -= money
        print(f'Снял {money}')


account = Bank('Артем', 100)

while True:
    print('Что хочешь сделать?')
    print('1 - пополнить')
    print('2 - cнять')
    print('q - выход')

    ans = input('Выбери действие')
    try:
        if ans == '1':
            money = int(input('Введи сумму: '))
            account.deposit(money)

        elif ans == '2':
            money = int(input('Введи сумму: '))
            account.withdraw(money)
        elif ans == 'q':
            break

    except ValueError as e:
        print(f'Ошибка {e}')
