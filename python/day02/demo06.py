dic = {
    1: 1,
    2: 1
}

count = 0

def fibonacci(n): # 5th -> 4th + 3rd 
    """이함수는 피보나치 수열을 구하기 위한 함수입니다."""
    if n in dic:
        return dic[n]
    else:
        global count
        count += 1 # count = count + 1
        output = fibonacci(n-1) + fibonacci(n-2) # f(5)
        dic[n] = output
        return output

# for i in range(1, 10 + 1):
#     print("fibonacchi({})={}".format(i, fibonacci(i)))
help(fibonacci)
print("------------------------------------")
print("fibonacchi({})={}".format(14, fibonacci(14)))
print("COUNT=",count)