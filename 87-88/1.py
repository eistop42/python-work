import pickle


class Car:
    def __init__(self):
        self.fuel = 100

    def drive(self, km):
        print(f'Проехали {km}')
        self.fuel -= 10

# car = Car()
# car.drive(5)
#
# with open('car_pickle', 'wb') as f:
#     pickle.dump(car, f)


with open('car_pickle', 'rb') as f:
    car = pickle.load(f)
    print(car.fuel)
    car.drive()

with open('car_pickle', 'wb') as f:
    pickle.dump(car, f)