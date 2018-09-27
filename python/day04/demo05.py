def calcsum(n):
    if n < 0:
        #raise ValueError("양의정수 사용")
        return -1

    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

#try:
result1 = calcsum(10)
if result1 == -1:
    print("양의 정수를 사용해 주세요.:")
else:    
    print("1~10 =", result1)

result1 = calcsum(-5)
if result1 == -1:
    print("양의 정수를 사용해 주세요.:")
else:    
    print("1~-5 =", result1)

#print("1~-5 =", calcsum(-5)) # return value -> 정수, ValueError
# except ValueError as ex:
#     print("양의 정수를 사용해 주세요.:")
    