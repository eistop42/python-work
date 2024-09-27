class Shop:
    PRODUCTS = {'колбаса': 20, 'молоко': 10}
    DISCOUNT = ['молоко']

    def __init__(self):
        self.count = 0
        self.all_sum = 0
        
    def buy(self, name):
        """Покупка продуктов"""
        name = name.lower()
        if name in self.PRODUCTS:
            price = self.PRODUCTS[name]
            if self._check_discount(name):
                price -= 5
            self.count += 1
            self.all_sum += price
            print(f'Купили {name}')
        else:
            print('ТАКОГО НЕТ БЛИН')

    def add_product(self, name, price):
        """Добавляем продукт в базу"""
        self.PRODUCTS[name] = price
        print('обновили базу')

    def delete_product(self, name):
        name = name.lower()
        if name in self.PRODUCTS:
            self.PRODUCTS.pop(name)
            print(f'Удалили {name}')
        else:
            print('Такого товара нет')

    def get_info(self):
        print(f'Всего купили на {self.all_sum}р.')
        print(f'Всего чеков {self.count}')
        print('Хорошего дня!')

    def _check_discount(self, name):
        """Проверили скидку"""
        return name in self.DISCOUNT


shop = Shop()
shop.buy('Колбаса')
shop.buy('Яйца')
shop.add_product('яйца', 100)
shop.buy('Яйца')
print(shop.PRODUCTS)
shop.buy('Молоко')
# shop.get_info()
shop.delete_product('Молоко')
print(shop.PRODUCTS)
shop.get_info()


