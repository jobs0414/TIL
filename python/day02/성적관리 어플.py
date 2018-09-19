def fibonacci(n): #5th -> 4th + 3rd 
    if n ==1: 
        return 1 
    elif n==2: 
        return 1 
    else: 
        retrun fibonacci(n-1)+fibonacci(n-2)

for i in range(1,5+1): 
    print("fibonacci({})={}".format(i,fibonacci(i))



