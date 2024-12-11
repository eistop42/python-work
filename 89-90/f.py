
def factorial(number):
    c = 1
    for i in range(1, number+1):
        c *= i
    return c

# f = factorial(5)
# print(f)

def factorial_r(number):
    if number == 1:
        return 1
    return number*factorial_r(number-1)

# 1. 5 * factorial_r(4)
# 2. 5 * 4 * factorial_r(3)
# 3. 5 * 4 * 3 * factorial_r(2)
# 4. 5 * 4 * 3 * 2 * factorial_r(1)
# 5. 5 * 4 * 3 * 2 * 1

print(factorial_r(5))

