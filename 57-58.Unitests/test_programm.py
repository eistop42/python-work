import unittest


class Calc:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        self.operations = 0

    def add(self):
        self.operations += 1

        return self.number1 + self.number2

    def subtract(self):
        self.operations += 1

        return self.number1 - self.number2

    def multiply(self):
        self.operations += 1
        return self.number1 * self.number2

    def divide(self):
        if self.number2 == 0:
            return 'Нельзя делить на нуль'
        return self.number1 / self.number2


calc = Calc(4, 5)
print(calc.add())


class CalcTestCase(unittest.TestCase):

    def test_add(self):
        calc = Calc(4, 5)
        res = calc.add()
        self.assertEqual(res, 9)

    def test_subtract(self):
        calc = Calc(4, 5)
        res = calc.subtract()
        self.assertEqual(res, -1)

    def test_miltiply(self):
        calc = Calc(4, 5)
        res = calc.multiply()
        self.assertEqual(res, 20)

    def test_operations_counter(self):
        calc = Calc(4, 5)
        calc.add()
        calc.add()
        calc.add()
        self.assertEqual(calc.operations, 3)

    def test_divide(self):
        calc = Calc(6, 3)
        self.assertEqual(calc.divide(), 2)

    def test_divide_zero(self):
        calc = Calc(6, 0)
        self.assertEqual(calc.divide(), 'Нельзя делить на нуль')


unittest.main()