class School:

    def set_classroom(self): 
        print("교실을 배정합니다.")

    def execute_test(self): 
        print("시험을 봅니다")






class Person: 

    def __init__(self): 
        print("사람데이터를 추가합니다.")


    def go2school(self): 
        print("학교를 간다")

    
    def lunch(self): 
        print("밥을 먹었다 1시에 밥먹는다.")


    def holiday(self): 
        print("휴일에는 학교에 가지 않음")

    
    def go2home(self): 
        print("집에 돌아 간다, 같이 퇴근하자")


    

class Student(Person,School): 
    
    
    def __init__(self): 
        print("학생 데이터를 출력합니다.")
        super().__init__()

    
    def study(self): 
        print(" 공부를 한다")

    def go2home(self): 
        print("오후 3시에 돌아갑니다.")


    def holiday(self): 
        print("휴일에는 학교안갑니다.")






class Teacher(Person,School): 

    def __init__(self): 
        print("선생님 데이터를 출력합니다.")
        super().__init__()



    def teach(self): 
        print("학생을 가르친다.")

    def go2home(self): 
        print("오후 6시에 돌아갑니다")

    def holiday(self): 
        print("휴일에도 학교간다")

# if __name__ == '__main__': 
#     Student(Person)

student1 = Student() 
teacher1 = Teacher() 


print("하루 학생의 하루 일과 ")
student1.go2home() 
student1.study()
student1.lunch()
student1.study()
student1.holiday()
student1.set_classroom()
student1.execute_test()



print("=====================")
print("하루 선생님의 일과 ")
teacher1.go2school()
teacher1.teach() 
teacher1.lunch()
teacher1.holiday()