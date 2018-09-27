import calendar

# 1. 년도, 월 입력 받은 후 해당 달력 출력 
# 2. 일월화수목금토 순서로 출력

import datetime 


def header(year,month): 
    # print('\t',year,'년',month,'월')
    print('\t{0}년 {1}월')
    print('-' * 30)
    print('일 월 화 수 목 금 토')
    # print('\t %s년 %s월')

def getStartPosition(year,month): 
    d=datetime.date(year,month,1)
    return d.weekday() #월요일 -> 0 


def getLastDay(year,month):
    if  month == 12: 
        year = year+1 
        month=1 
    else: 
        month=month+1

    next_month = datetime.date(year,1)  
    t = datetime.timedelta(days = 1)
    gap= next_month-t 
    print(next_month)
    print(gap)  # 2018-10-01   - 1 day   = 2018 -9 -30 
    return gap.day


# 31 28 31 30 31 30 31 31 30 31 30 31 -> 9월달 찾기 


def display(year,month):
    header(year,month)
    startPos=getStartPosition(year,month) #1에 해당하는 요일이 어디인지 확인하기 위해서 
    lastDay=getLastDay(year,month)
    # ex 9월달 1일 토요일 -> startPos = 5 
    # 1~30까지 출력 + 1일 앞에 몇일의 공백이 오는지 출력. 
    totalDays=startPos+ lastDay +1  # +1을 왜할까요?!
    #1~6개는 공백을 출력하고 
    # 7번째 ~ 마지막번째(30) -> 순서대로 출력 (단, 7번째 마다 개행)
    # 단 전체 데이터는 7번째 마다 개행 
    d=1
    for d in range(1,totalDays+1):

        if d <= ((startPos+1) % 7):
            print('{:>2}'.format('*'),end=' ')

        # elif n%7 ==0: 
        #     print()

        else: 
            print('{:>2}'.format(d),end=' ')
            d=d+1
       #-----------------------
        if n%7 ==0: 
            print()


        # if startPos=7: 
        #     print(""*6,1)


        # elif d%7==0: 
        #     print(d,"\n")
    

        # else: 
        #     print(d,end=' ')






    #공백은 6개 출력하되 7개씩 끊어서 데이터 출력 


def main(): 
    year=int(input('연도를 입력해주세요 ex. xxxx -> '))
    month=int(input("월을 입력하세요 ex) (1~12) ->"))
    display(year,month)


    print() 


main()