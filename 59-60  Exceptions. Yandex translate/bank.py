# class AmountError(ValueError):
#     pass

def deposit(money, balance):
    if money < 0:
        raise ValueError('Сумма должна быть положительной')
    balance += money
    return balance

balance = 0

while True:
    try:
        money = int(input('Сколько денег зt(акинуть? '))
        balance = deposit(money, balance)
    except ValueError as e:
        print(f'Что-то пошло не так... {e}')
    print(f'Твой счет: {balance}')
