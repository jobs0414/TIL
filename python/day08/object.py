# 쇼핑몰을 만들고 싶다. 
# 상품 / 관리자 / 사용자 / 
# 상품을 사기 위한 동작 
# 사람도 표현 동물도 표현 가능. 

# object orient program 
# 오브젝트가 가지고 있는 특징 
# 자동차가 가지고 있는 타이어 개수 색상 핸들의 위치 엔진의 크기 모두 특징  ===속성 
# 오브젝트의 기능을 나타내고 있는 것이 === 기능 
# 관련된 속성과 동작을 하나의 범주로 묶어 실세계의 사물을 흉내냄. 

# 속성 >> 특징(데이터)     동작 >> 기능    function >> method 

# 클래스 모델링 

# 성적관리 
# object 
# 학생이라는 것 자체가 object 학생 >> 이름 ,시험 성적 국영수 , 성별 , 
# 동작 기능 >> 성적 석차 총점 

# 분석과 설계 
# 필요한 속성과 동작들을 쭉 나열하게 오브젝트와 오브젝트의 결과를 나열 
# 모델링 : 사물 분석하여 필요한 속성과 동작 추출 
# 캡슐화 : 모델링 결과를 클래스로 포장 
# 객체는 모든 것을 표현할 수 있음. 
# 사물의 속성은 변수로, 동작은 함수로 표현. 

# 속성은 변수로 동작은 함수로 
# 변수와 함수를 객체로 부르는 것 . 

# class 설계도면 
# 어떻게 만들 겁니다. 
# object ----> 자료형 ------> class 화  ------> 설계도면 
# 이 과정들을 instance 화라 부를 겁니다. 

# class는 object를 만들기 위핸 것 
# 실체화 하기위한것  instance 
# class 에서 만든 것 인스턴스 
# 인스턴스 == object라 봐도 틀리지는 않다. 


# 멤버 
# -

# 생성자 : 클래스 선언 형식 








# class Person:
#     def __init__(self,age,name):          #초기화 관련된 함수  # 객체 생성시  필요한 초기화 작업 
#         print("call init method")
#         self.name=name
#         self.age=age

#     def intro(self):   #모든 클래스에는 self 가 들어간다.  
#         print('{0} {1}살'.format(self.age,self.name))


# a= 'Hello'  #문자열, 숫자형, 불린(boolean)

# hong1 = Person('홍길동',40)  #클래스 타입 생성시킨 것에 불과 #객체에 생성 구문  self 에 전달 
# hong1.intro()

# kang1 = Person('강감찬',50)
# kang1.intro() 


# class 이름 : 
#     def__init__(self,초기값): 
#     멤버 초기화 
#     메서드 정의 


#human.py 
#40살 홍길동, 60살 강감찬 
#Person , Human 


# print('{0}살 {1}'.format(40,'홍길동'))
# print('{0}살 {1}'.format(60,'강감찬'))
#한번 출력되고 끝이다. 

#객체는 속성과 기능을 가지고 있다 .
#객체 = 속성 + 기능 (Method ))

# 객체 지향 프로그래밍 - 객체와 클래스 
class Car: 
    def __init__(self,color): 
        self.color = color
        self.wheel_size= 16 
        self.engine = 2000 

    def forward(self): 
        pass 

    def backward(self): 
        pass

    def turn_left(self): 
        pass 

    def turn_right(self): 
        pass 

    @STATICMETHOD # 더이상 Self 를 갖지 않고 인스턴스에 종속되지 않는다. 
    def company_name(): 
        print("Samsung Muticampus and HP")

if __name__ == '__main__':
    my_car =Car(0xAAFF00) 
    Car.company_name()

    my_car.color = 0x00FF00  # 인스턴스 변수, 객체 변수 
    print('0x{:02X}'.format(my_car.color))
    print(my_car.wheel_size)
    print(my_car.engine)


    my_second_car =Car(0x11FF00) 

    print(my_second_car.color)
    print(my_second_car.wheel_size)
    print(my_second_car.engine)
    


    my_car.forward()
    my_car.backward()
    my_car.turn_left()
    my_car.turn_right()




