# python/day05/calculator.py 

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("!!! 0으로 나눌수 없습니다.")
        # raise ZeroDivisionError
    else:
        return a / b