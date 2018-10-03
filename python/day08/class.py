class Student:

    #생성자 메소드 

    def __init__(self,name,kor,mat,eng,science):
        self.name = name 
        self.kor = kor 
        self.mat = mat 
        self.eng = eng 
        self.science = science


    def get_sum(self):   # self.name , self.kor , self.eng , self.mat 
        return self.kor + self.mat + self.eng + self.science
        
    # 평균을 구하는 메소드를 구해보자 

    def get_average(self):  # self.name self.kor self.eng self.mat 
        average = self.get_sum() /4    # self가 가지고 있는 
        return average 

    def to_string(self): 
        return '{0}\t{1}   {2}'.format(self.name,self.get_sum(),self.get_average())


    def study(self): 
        print("공부 합시다")


class Teacher: 
    print("난 선생이다")



students = [
    
    Student('홍길동',90,80,70,60),
    Student('한상',90,100,95,90),
    Student('김상',90,40,70,60),
    Student('김동',90,50,10,60)

]

for student in students: 
    print(student.to_string())

print(isinstance(students[0],Student))

classroom = [    Student('한상',90,100,95,90),
                Student('김상',90,40,70,60),
                Teacher(),
                Teacher(), 
                 Student('김동',90,50,10,60)
    
]

for person in classroom: 
    if isinstance(person,Student): 
        person.study() 

    elif isinstance(person,Teacher): 
        person.teach() 

    else: 
        print()


# print(students[0].get_sum())
# print(students[1].get_sum())
print(students[0].to_string())
print(isinstance(students[0],Student))   # isinstance 입니까? 

self 