def add_message(function, *args, **kwargs):
    def func(*args, **kwargs):
        print('Кто вызвал функцию!')
        return function(*args, **kwargs)

    return func
@add_message
def add(number1, number2):
    print(number1 + number2)

@add_message
def subtract(number1, number2):
    print(number1 - number2)


add(1,5)
subtract(3,5)

