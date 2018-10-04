# def add(a,b): 
#     print(a+b)


# plus =add
# plus(10,20)


def calc(op, a, b): 
    pass 


def add(a,b): 
    print(a+b)


def substract(a,b): 
    print(a-b)

calc(add,10,20)

#파라미터로 함수를 해도 괜찮더라 



# 
#독립적으로 해야 함 .쏘여 험. 




def add(a,b): 
    return a+b 





def calcsum(n): 
   
    sum=0 
    for i in range(n+1):
        sum= add(sum, i)

    return sum 

print('1~10=', calcsum(10))














