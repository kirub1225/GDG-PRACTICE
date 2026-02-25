from functools import reduce

def factorial(num):
    result = reduce(lambda x, y: x * y, range(1, num + 1))
    print(result)

num = int(input("enter a number: "))