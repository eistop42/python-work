#
# Создайте класс BankAccount,
# который содержит атрибуты: owner (владелец счета) и закрытый атрибут _balance (баланс).
# Добавьте методы для пополнения (deposit) и снятия денег со счета (withdraw).
#
#  Ограничьте возможность снятия суммы, превышающей баланс.
#
# Добавьте метод для вывода текущего баланса, используя инкапсуляцию.


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def __str__(self):
        return self.owner

    def deposit(self, sum):
        self._balance += sum
        print(f'Добавили {sum}. Теперь {self._balance}')

    def withdraw(self, sum):
        if sum <= self._balance:
            self._balance -= sum
            print(f'Cняли {sum}. Теперь {self._balance}')
        else:
            print('Не хватает :(')

    def get_balance(self):
        return self._balance


class Bank:
    """Банк для хранения аккаунтов"""
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(self.accounts)

    def get_all_sum(self):
        sum = 0
        for account in self.accounts:
            sum += account.get_balance()
        print(f'Всего денег на счетах: {sum}')


account1 = BankAccount('Том', 100)
account2 = BankAccount('Джек', 500)

bank = Bank()

bank.add_account(account1)
bank.add_account(account2)

bank.get_all_sum()

print(account1)
print(account2)
