import pymysql


conn = pymysql.connect(host='127.0.0.1',user='root',password='',db='test_python', charset='utf-8')  # mysql (remote) -> url, user, password 
cursor = conn.cursor() 

def conncetion(con,cursor): 
   
    print(con,"데이터베이스 연결 성공")
    return con,cursor

def create():
    con=sqlite3.connect('user11.db')
    cursor=con.cursor
    cursor.execute("""create table tblAddr1(
    name CHAR(10) PRIMARY KEY, 
    phone CHAR(15), 
    addr TEXT
    
    )""")

    return 


def select(sql1): 

    sql1="SELECT FROM tblAddr1"
    return sql1


def update(sql2): 

    sql2="UPDATE SET tblAddr set addr='london' where name='상우'"
    return sql2


def main():
    create()
    conncetion()
    update(sql2)
    select(sql1)


main()
