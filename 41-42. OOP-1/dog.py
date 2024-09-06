class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 50
        self.food_to_eat = ['мясо', 'корм', 'печеньки']
        self.friend = None
        self.human = None

    def eat(self, food):
        if food in self.food_to_eat:
            self.health += 5
            print('Спасибо!')
        else:
            print('Я такое не ем')
    def walk(self):
        """Погулять"""
        self.health += 5
        print('Ура, я поглял(a)')

    def get_human_age(self):
        """Получить человеческие года"""
        return self.age * 7

    def get_friend(self, dog):
        """Подружиться с собакой"""
        if abs(dog.age - self.age) < 3:
            print('Теперь ты мой друг')
            self.friend = dog
            dog.friend = self
        else:
            print('не получится...')

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 60
        self.dog = None

    def add_dog(self, dog):
        if not dog.human and not self.dog:
            self.dog = dog
            dog.human = self
            print('мЫ пОдРуЖиЛиСь11!')
        else:
            print('не получится...')


dog1 = Dog(name='Тузик', age=2)
dog2 = Dog(name='Чарли', age=4)


dog1.get_friend(dog2)
print(dog1.friend.name)
print(dog2.friend.name)

# пытаемся подружиться с собакой
human = Human('Джек', 23)
human.add_dog(dog1)
human.add_dog(dog2)


# dog1.eat('мясо')
# dog1.eat('брокколи')
# dog1.walk()
# print(dog1.health)
# print(f'возраст: {dog1.get_human_age()}')
