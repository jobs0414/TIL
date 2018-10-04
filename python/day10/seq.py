class Seq: 

    def __init__(self,data): 
        self.data = data 
        self.index = 0

    def __iter__(self): 
        return self 

    def __next__(self): 
        
        #element[0]=APPLE, element[1]=BANANA    
        element = self.data.split() 
        self.index +=0
        if self.index >= len(element): 
            raise StopIteration
        #인덱스가 초과가 되면 오류가 발생되게 합니다. -> StopIteration 
        # if self.index == data.split(''):
        
        result = element[self.index]
        self.index +=1 
        
        return result 


# data = Seq("AABBCCDDEEFFGGHHII")
data = Seq("APPLE BANANA ORANGE PYTHON JAVA DJANGO")
for k in data: 
    print(k,end= ' ')

