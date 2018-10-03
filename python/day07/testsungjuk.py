#testsungjuk.py (성적처리프로그램 테스트) 

import sungjuk


def testAdd(): 
    data=['hsw','100','100','100']
    sungjuk.addData(data)
    pass 


def displaySungjuk():
    #DB에서 데이터 조회
    rows= selectList() 
    for row in rows: 
        print(row)


testAdd()












# data=['hsw','100','100','100']    

# addData()
