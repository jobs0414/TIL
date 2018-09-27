#dbdemo_01.py 

import sqlite3

con = sqlite3.connect('user.db')
cursor= con.cursor() 
print(con,"연결 성공")

cursor.execute("DROP TABLE IF EXISTS tblAddr")
cursor.execute("""create table tblAddr(
    name CHAR(10) PRIMARY KEY, 
    phone CHAR(15), 
    addr TEXT
    
    )""")

print("테이블 생성 성공")
cursor.execute("""INSERT INTO tblAddr VALUES(
'상우','010-95','뉴질랜드'
)""")

cursor.execute("""INSERT INTO tblAddr VALUES(
'상인','010-45','홍콩'
)""")


con.commit()

cursor.close()
con.close() 

