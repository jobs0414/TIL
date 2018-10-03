
INCH = 2.54 

def calsum(n): 
    sum=0 
    for i in range(n+1):  # n=10, 0~9 
        sum += i 

    return sum  

if __name__ == '__main__': 
    print('__name__=' + __name__)
    print("인치=", INCH)
    print("합계=",calsum(10))


