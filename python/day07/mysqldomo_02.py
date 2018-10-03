import pymysql 

#1. Connection 

conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='test_python', charset='utf-8')  # mysql (remote) -> url, user, password 

cursor = conn.cursor() 

inputId = imput('아이디를 입력하여주세요')
inputPwd=input('비밀번호를 입력하여주세요')


#string interpolation -> parameter placeholder 
sql= "%s %s %s" %('test','test','test')

insertSql= 'Insert Into member(id,pwd,name,datetime) 
selectSql = 'SELECT * FROM member where id=%s pwd=%s'                       #파라미터로 받는 방법을 쓰자.  
print(selectSql)
cursor.execute(selectSql)
row= cursor.fetchone() 


if row == None :
    print("로그인 실패 !! id나 pwd가 잘못되었습니다.")

else: 
    print("로그인 성공!!",row)



cursor.close() 
conn.close() 

