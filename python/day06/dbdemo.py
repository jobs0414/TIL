#dbdemo_01.py 

import sqlite3

con = sqlite3.connect('user.db')
cursor= con.cursor() 
print(con,"연결 성공")



cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""create table sungjuk( 
	idx integer primary key auto_increment, 
	name varchar(20) not null, 
	kor integer, 
	eng integer, 
	mat integer, 
	reg_date timestamp
    
)""")


cursor.execute("""insert into sunguk(name,kor,eng,mat,reg_date) values('user1',100,90,80,now()""")
cursor.execute("""insert into sunguk(name,kor,eng,mat,reg_date) values('user2',50,70,80,now()""")
cursor.execute("""insert into sunguk(name,kor,eng,mat,reg_date) values('user3',100,100,100,now()""")
cursor.execute("""insert into sunguk(name,kor,eng,mat,reg_date) values('user4',70,95,85,now()""")
cursor.execute("""insert into sunguk(name,kor,eng,mat,reg_date) values('user5',60,90,80,now()""")













# print("테이블 생성 성공")
# cursor.execute("""INSERT INTO tblAddr VALUES(
# '상우','010-95','뉴질랜드'
# )""")

# cursor.execute("""INSERT INTO tblAddr(name,phone,addr) VALUES(
# '상인','010-45','홍콩'
# )""")


# print("확인")
con.commit()

cursor.close()
con.close() 

