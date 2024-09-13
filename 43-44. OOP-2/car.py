

class Car:
    def __init__(self, color, fuel, consumption, mileage=0):
        self.color = color
        self.fuel = fuel
        self.consumption = consumption
        self.mileage = mileage
        self.is_clean = False
        print(f'Создали машину {self.color, self.fuel}')

    def drive(self, km):
        need_fuel = (km*self.consumption)/100
        if need_fuel <= self.fuel:
            print(f'Проехали {km} км')
            self.fuel -= need_fuel
            self.mileage += km
        else:
            print('Не доедем :)')

    def get_mileage(self):
        return self.mileage

    def clean(self):
        self.is_clean = True


class SportCar(Car):

    def fast_drive(self, km):
        need_fuel = (km * self.consumption*2) / 100
        if need_fuel <= self.fuel:
            print(f'Проехали {km} км')
            self.fuel -= need_fuel
            self.mileage += km
        else:
            print('Не доедем :)')

    def clean(self):
        if self.is_clean == True:
            print('Она уже чистая')
        else:
            self.is_clean = True


car = Car(color='желтый', fuel=20, consumption=5)
sport_car = SportCar(color='зеленый', fuel=20, consumption=15)

sport_car.fast_drive(50)
car.clean()
sport_car.clean()
sport_car.clean()