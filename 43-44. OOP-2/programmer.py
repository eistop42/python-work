
class Programmer:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

        self.all_salary = 0
        self.all_time = 0
        self.SALARY_INFO = {'Junior': 10, 'Middle': 15}

    def work(self, time):
        self.all_time += time
        salary = self.SALARY_INFO['Junior']
        self.all_salary = time * salary
        print(f'Отработал {time}')

    def info(self):
        print(f'{self.name} {self.all_time}ч. {self.all_salary}тгр.')

prog = Programmer('Василий Иванов', 'Junior')
prog.work(100)
prog.info()