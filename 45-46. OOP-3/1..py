

class MyInt(int):
    def __add__(self, other):
        return self - other

    def add_number(self, number_2):
        return self - number_2

a = MyInt(4)
b = MyInt(5)
print(a.add_number(b))
# print(a+b)
