##쌤 풀이 
import random 

com=random.randrange(1,100)
count=0 
point=0

while True:  #무조건 실행이 되어야 한다는 뜻 
    my=int(input("숫자 입력하라우(1~100)"))
    count+=1
    
    if my<1 or my>100: 
      print("1~100을 입력해주세요")
      count
    
    else:     
        if my>com: 
            print("보다 작은 숫자 입력해주세요")
        
        elif my<com: 
            print("보다 큰 숫자를 입력해주세요")
        
        else: 
            print("맞추었다")
            break #근접해 있는 Loop 실행 종료 

      
print("===================")
print("COMnum=",com)
print("축하합니다 총",count, "번에 맞추셨습니다.")