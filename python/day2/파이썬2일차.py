dic={
    1:1,
    2:1

}
count=0

def fibonacci(n): 
    print("fibonacci{}를 구합니다.".format(n))
    
    if n in dic:
        return dic[n] 

    else: j

        global count 
        count += 1 
        output= fibonacci(n-1)+fibonacci(n-2)  #f(5)
        dic[n] = output 
        return output 

print("------------------------")
print("fibonacci({})")

help(fibonacci)