sungjuk={}

while True:  #무한루프가 도는 것 항상 true니까 
    print("##현재 등록자 수 :",len(sungjuk))
    cmd = int(input('1) 성적입력 2) 성적출력  3)성적조회 (1~3) -> '))
    if cmd ==1: 
        for count in range(3):
            userData = input("성적을 입력하세요. (이름,국어,영어,수학) ->")
            data=userData.split(',')
            print(data) #['홍길동','100','90','70']
            #sungjuk['name'] = ['100','20','50']
            sungjuk[data[0]] = data[1:]
            print(sungjuk[data[0]],"=",len(sungjuk))

    elif cmd ==2: 
    #정보 출력 sungjuk(3)
        for student in sungjuk: 
            print(student,':',sungjuk[student])

    elif cmd ==3: 
    #정보 조회 -> 조회 
        searchuser=input("검색할 학생의 이름을 입력하세요->")
        print(sungjuk[searchuser])

    else: 
        print("잘못된 명령어 입니다. 다시 입력해주세요")
        continue
2
