# demo10_09.py (class decorator)

class Outer: 
    def __init__(self,func): 
        self.func = func 

    def __call__(self): 
        print("-"*15)
        self.func()
        print("-"*15)


def inner(): 
    print("출력입니다")

inner = Outer(inner)
inner() 

