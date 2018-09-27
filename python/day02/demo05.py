# def sum_all(start=1, end=100): # parameter 지정? 
#     result = 0
#     for i in range(start, end): # start <= i < end
#         result += i
#     return result

# print("1 to 100=", sum_all(end=100)) # 1 to 100=5050
# print("1 to 1000=", sum_all(end=1000)) # 1 to 100=5050
# print("1 to 10000=", sum_all(end=10000)) # 1 to 100=5050
# print("50 to 100=", sum_all(50, 100)) # 1 to 100=5050

# def factorial(n): 
#     output = 1 
#     for i in range(1, n + 1): # 1 <= i < n + 1 -> (1 <= i <= n)
#         output *= i
#     return output
# print(factorial(5)) # 1 x 2 x 3 x 4 x 5

def factorial(n):
    if n == 1:
        return 1
    elif n > 1: # = n * (n-1)
        return n * factorial(n-1)

print("1!=", factorial(1))
print("3!=", factorial(3))
print("5!=", factorial(5))