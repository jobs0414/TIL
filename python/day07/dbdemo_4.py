import sqlite3

con=sqlite3.connect('user.db')
cursor=con.cursor
    
    
def selectData():

    sql1='SELECT * FROM tblAddr'
    cursor.execute(sql1)
        
    while True: 
        row = cursor.fetchone() 
        if row == None: 
            break
        
        print('이름:%s,전화번호:%s,주소:%s' % row)



def updateData(isInsert): 
    
    if isInsert == True: 
        sql= "INSERT"
    else: 
        sql = "UPDATE"


    cursor.execute(sql)
    con.commit() 
    print(isInsert,"성공!")
 



def closeConnection(): 
    cursor.close() 
    con.close() 




def main():
    selectData()
    updateData()
    selectData()
    closeConnection() 
