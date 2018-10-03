class Parent: 
    def parent_method(self): 
        print("parent method")



class Child(Parent): 
    def child_method(self): 
        print("child method")

p= Parent()
p.parent_method() 

c=Child() 
c.child_method() 
c.parent_method() 
