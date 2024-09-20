class Shop:
    PRODUCTS = {'колбаса': 100}

    def __init__(self):
        self.count = 0
        self.all_sum = 0
    def buy(self, name):
        """Покупка продуктов"""
        name = name.lower()
        if name in self.PRODUCTS:
            self.all_sum += self.PRODUCTS[name]
            self.count += 1
            print(f'Купили {name}')
        else:
            print('ТАКОГО НЕТ БЛИН')

    def add_product(self, name, price):
        """Добавляем продукт в базу"""
        self.PRODUCTS[name] = price
        print('обновили базу')

    def get_info(self):
        print(f'Всего купили на {self.all_sum}р.')
        print(f'Всего чеков {self.count}')
        print('Хорошего дня!')

shop = Shop()
shop.buy('Колбаса')
shop.buy('Колбаса')
shop.buy('Яйца')
shop.add_product('яйца', 100)
shop.buy('Яйца')
shop.get_info()

