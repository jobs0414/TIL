def output(func): 
    def wrapper(): 
        print("-" * 15)
        func()
        print("-" * 15)

    return wrapper



@output
def inner(): 
    print("결과입니다.")

inner()




