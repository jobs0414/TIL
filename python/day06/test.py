#test.code.py 

# import my_calendar as cal

# def test(): 
#     print(cal.getLastDay(2018,9))
#     print(cal.getLastDay(2018,12))
# test() 


# for c in range(ord('a'),ord('z')+1):
#     print(chr(c),end='  ')
# 
# 
import datetime

def getStartPosition(year,month): 
    d=datetime.date(year,month,2)
    return d.weekday() 

print(getStartPosition(2018,10))