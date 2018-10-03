from bs4 import BeautifulSoup
from urllib import request
import sqlite3
from weather import Weather 

conn = pymysql.connect(host='127.0.0.1',user='root',password='',
db='test_python', charset = 'utf-8')

cursor = conn.cursor(pymysql.cursors.DictCurosr)
print("###1. dB연결 완료 ")


target = request.urlopen("http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=108")
print(target, type(target))
soup = BeautifulSoup(target, "html.parser")


for location in soup.select("location"):
    if location.select_one("city").string == '서울':
        
        city= location.select_one("city").string
        for data in location.select("data"):
            # print("City: ", data.select_one('city').string)
        #1)   Weather 객체 생성 (13개)  -> db 저장
        
            weather = Weather(1, 
                        city,
                        data.select_one('tmef').string,
                        data.select_one('wf').string,
                        data.select_one('tmn').string,
                        data.select_one('tmx').string
                        

                        )

        
        SQL = """INSERT INTO weather(location,fc_date,description,temp_min,temp_max
               VALUES(%s,%s,%s,%s,%s)
                """

        cursor.execute(SQL, (weather.location))

        # my think 
        #     list_a = [
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],
        #         ['서울','2018-10-1','구름 많음','20','25'],

                 
        #          #...13개 저장
        #     ] 

            
        # for list_a in SQL:
        #     print(list_a) 







            print("Date: ", data.select_one('tmef').string, end='\t\t')
            print("Weather: ", location.select_one('wf').string, end='\t')
            print("Temperature_Min: ", location.select_one('tmn').string, end='\t')
            print("Temperature_Max: ", location.select_one('tmx').string, end='\t')
            print()