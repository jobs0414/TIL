import sqlite3
import pymysql


con = sqlite3.connect('user12.db')
cursor= con.cursor(pymysql.cursor.DictCursor)



def displaySungjuk(searchUser):

    if len(searchUser) ==0: 
        #전체 사용자ps  
        selectSql="""SELECT name,kor,eng,mat,(kor+eng+mat)/3 as average 
    From sungjuk ORDER BY total DESC """

        cursor.execute(selectSql)


    else: 
         selectSql="""SELECT name,kor,eng,mat,(kor+eng+mat)/3 as average 
        From sungjuk where name=%s 
        order by total desc"""
        cursor.execute(selectSql,searchUser)
       

       
       
        #개별 사용자 검색


    #DB에서 데이터 조회
    rows= selectList(searchUser) 
    return rows 

    for row in rows: 
        # print("%s\t%s\t%s\t%s\t")
         print("{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(
         row['name'],row['kor']],row['eng'],row['mat'],row['total'],row['average']))
        

    pass 

def selectList(searchUser): 
    
    selectSql= """SELECT name,kor,eng,mat,(kor+eng+mat)/3 as average 
    From sungjuk ORDER BY total DESC """

    cursor.execute(selectSql)
    rows= cursor.fetchall() 
    for row in rows: 
        print(row)

    #조회 

    pass 
    





def selectOne(searchUser): 
    pass


def addData(data):  #['홍길동','100','200','300']

    insertsql = """insert into sungjuk(name,kor,eng,mat,reg_date)
                values(%s,%s,%s,now()))""" 

    cursor.execute(insertsql,(data[0],data[1],data[2],data[3]))



    insertSql = """INSERT INTO sungjuk(name,kor,eng,mat,reg_date)
                VALUES(%s,%s,%s,%s,NOW())"""

   
    cursor.execute(insertSql,(data[0],data[1],data[2],data[3]))
    con.commit() 
    print(" ### 사용자 정보 추가 성공")
    pass 




def closeConnection(): 
    cursor.close()
    con.close() 




def main(): 
        
    while True:
        print("## 현재 등록자 수:")
        # 1. 입력값이 숫자(1~4) 인지 확인
        try:
            cmd = int(input('1) 성적입력 2) 성적출력 3) 성적조회 4) 종료 (1~4) ->'))
            #isValid = validateNumber(cmd, 1, 4)
        except:
            print("** 명령어는 1~4 사이의 숫자를 입력해야 합니다. **")
            continue

        if cmd == 1:
            # 2. 이름 뒤에 3개의 과목인지, ','로 구분되어 있는지 
            # 3. 각 과목의 점수는 0~100 
            while True:
                try:
                    userData = input('성적을 입력하세요. (이름,국어,영어,수학) ->')        
                    data = userData.split(',') # len(data) = 4
                    if len(data) != 4: #NG
                        raise Exception
                    else: #OK
                        try:
                            #isValid = validateNumber(data[1], 0, 100)
                            #isValid = validateNumber(data[2], 0, 100)
                            #isValid = validateNumber(data[3], 0, 100)

                            kor = int(data[1])
                            eng = int(data[2])
                            mat = int(data[3])

                            if kor < 0 or kor > 100:
                                raise Exception
                            if eng < 0 or eng > 100:
                                raise Exception
                            if mat < 0 or mat > 100:
                                raise Exception
                        except:
                            raise Exception        
                except Exception as ex:
                    print("** 성적데이터를 정확하게 입력해 주세요. **")
                    continue
                else:       # if ~ else
                    print(data) #['홍길동', '100', '90', '70'], data[1:]
                    #db에 저장 
                    addData(data)
                    
                    break
        elif cmd == 2:
            print('이름\t국어\t영어\t수학\t총점\t평균')
            



            displaySungjuk()
        elif cmd == 3:
            # 정보 조회 -> 출력 
            searchUser = input("검색할 학생이름을 입력하세요->")
            print(sungjuk[searchUser])
            # DB 검색 
            selectOne(searchUser)


        elif cmd == 4:
            quit()
        
        else:
            print("잘못된 명령어 입니다. 다시 입력해 주세요.")
            continue

      
main()



