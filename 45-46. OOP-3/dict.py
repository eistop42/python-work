
"""Слвоари"""
a = {'Молоко': 100, 'Колбаса': 20}

"""Итерация по ключам"""
for key in a:
    print(key)

"""Итерация по ключу и значению"""
for key, value in a.items():
    print(key, value)

"""Принадлежность"""
if 'Молоко' in a:
    print('Молоко есть')