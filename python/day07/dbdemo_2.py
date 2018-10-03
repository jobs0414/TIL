import sqlite3

con = sqlite3.connect('user1.db')
cursor=con.cursor() #메소드를 사용할때 () 


# DML - CRUD (insert, select , update, delete)
sql1='SELECT * FROM tblAddr'
cursor.execute(sql1)

# fetchall(), fecthone() , fetchmany() 
# SELECT * FROM tblAddr WHERE name='이도원'

# table= cursor.fetchall() 
# #print(type(table)) 
# print(table)

# for row in table: 
#     #print('이름:{0},전화번호:{1},주소:{2}'.format(row[0],row[1],row[2]))
#     print('이름:%s,전화번호:%s,주소:%s' % row)

#fetch one으로 데이터 가지고 오는 법  

while True: 
    row = cursor.fetchone() 
    if row == None: 
        break

    print('이름:%s,전화번호:%s,주소:%s' % row)


updateSql= "UPDATE tblAddr set addr='서울' where name='상우'"
cursor.execute(updateSql)
con.commit() 

print("수정 성공")





cursor.close()
con.close()

