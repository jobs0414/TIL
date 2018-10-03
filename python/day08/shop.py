########온라인 쇼핑에 사용되는 회원의 종류를 모델링 하려고 한다. 

#database connection 


class Member: 

    def __init__(self,search,additem,buyproduct,buyproduct2,listproduct,sumpoint)
        self.search = search 
        self.additem =additem
        self.buyproduct = buyproduct
        self.buyproduct2 = buyproduct2
        self.listproduct = listproduct
        self.sumpoint = sumpoint 
        

    
    def login(self): 
        print("{0}로 로그인이 되었습니다.".format(login))
        #DB check with ID, PWD 



    def logout(self): 
        print("{0}님이 로그아웃 되셨습니다.".format())


    
    def search(self,item_name): 

        data_list = """select * from shop where=shoes"""
        for data in data_list: 
            print(data_list)


    def additem(self): 
        
        


    def buyproduct(self): 
        input_bucket = 



    def buyproduct2(self): 
        pass 



    def listproduct(self): 
        pass 

    def sumpoint(self): 
        
        
        point = 



    


class Premium(Member): 
    
    def search(self):
        
    def sumpoint(self):
        
        if sumpoint>10000000:
            discount=0.1   
            print("할인 적용:{0}".format(discount))
        

        
        elif sumpoint>5000000:
            discount=0.15 
            print("할인 적용:{0}".format(discount))

        
        elif sumpoint>1000000: 
            print("할인 적용:{0}".format(discount))



    










