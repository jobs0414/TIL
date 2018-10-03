import pymysql
#1. Connection 

conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='test_python', charset='utf-8')  # mysql (remote) -> url, user, password 

cursor = conn.cursor() 

insertSql = """INSERT INTO member(id,pwd,name,reg_date) VALUES('admin','1234','Administrator',NOW())"""



cursor.execute(insertSql)
data = cursor.fetchall() 


for row in data: 
    print(row)

conn.close() 


#2. Cursor 

#3. Execute SQL
