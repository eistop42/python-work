
class Programmer:
    SALARY_INFO = {'Junior': 10, 'Middle': 15, 'Senior': 20}

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        self.hours_to_do = 0
        self.all_salary = 0
        self.all_time = 0
        self._extra_salary = 0

        # дефолтная зп
        self.salary = self.SALARY_INFO[self.grade]

    def work(self, time):
        self.all_time += time
        salary = self.salary * time
        self.all_salary += salary
        print(f'Отработал {time}')
        self._check_bonus()

    def rise(self):
        if self.grade == 'Junior':
            self.grade = 'Middle'
            self.salary = self.SALARY_INFO[self.grade]

        elif self.grade == 'Middle':
            self.grade = 'Senior'
            self.salary = self.SALARY_INFO[self.grade]

        elif self.grade == 'Senior':
            self.salary += 1

    def info(self):
        print(f'{self.name} {self.all_time}ч. {self.all_salary}тгр.')

    def _check_bonus(self):
        if self.all_time >= 1000:
            self.all_salary += 10000

class Project:
    def __init__(self, name):
        self.name = name
        self.programmers = []

    def assign_programmer(self, programmer):
        """Добавляем программиста в проект"""
        self.programmers.append(programmer)
        print(f'Добавил {programmer.name}')

    def add_hours(self, hours):
        """Добавляем часы работы всем программистам"""
        for programmer in self.programmers:
            programmer.hours_to_do += hours

    def get_salary(self):
        """Cчитаем сумму всех затрат на проект"""
        all_salary = 0
        for programmer in self.programmers:
            salary = programmer.hours_to_do * programmer.salary
            all_salary += salary
        return all_salary


project = Project(name='Сайт')

programmer1 = Programmer('Васильев Иван', 'Junior')
programmer2 = Programmer('Васильев Том', 'Middle')
programmer3 = Programmer('Васильев Джон', 'Senior')

project.assign_programmer(programmer1)
project.assign_programmer(programmer2)
project.assign_programmer(programmer3)

project.add_hours(10)

print('Денег потребуется', project.get_salary())