def hello(count):
    if count == 500:
        print('ура')
        return
    count += 1
    print(f'привет {count}')
    hello(count)

hello(0)


