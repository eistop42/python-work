import random


class RedButton:
    def __init__(self):
        self.clicks = 0

    def click(self):
        print('Тревога')
        self.clicks += 1

    def count(self):
        return self.clicks

    def bang(self):
        boom = random.randint(0,1)
        if random.randint(0,1) == 1:
            print('Бум!!!!!!!')
        else:
            print('Осечка...')

first_button = RedButton()
second_button = RedButton()

for i in range(5):
    if i % 2 == 0:
        first_button.click()
    else:
        second_button.click()
print(first_button.count(), second_button.count())
first_button.bang()
second_button.bang()