# python 첫째 날

## 1. Python webbrowser

1. `webbrowser` 모듈 사용법 

```python
import webbrowser
webbrowser.open("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=아이유")
webbrowser.open("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=신소율)
webbrowser.open("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=신소율")
```

2. `webbrowser` 코드 깔끔히

   ```python
   import webbrowser 
   
   keywords={'신소율','TED','오박사블로그'}
   url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
   
   print("url+keywords[0]")
   
   print("url+keywords[1]")
   
   print("url+keywords[2]")
   ```

   3.`webbrowser` 코드 다시

   ```python
   import webbrowser 
   
   keywords={'신소율','TED','오박사블로그'}
   url="https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
   
   for name in keywords:
   webbrowser.open(url+name)
   
   ```

### 코스피 스크래치

```python
import requests
from bs4 import BeautifulSoup
url = 'https://finance.naver.com/sise'
res = requests.get(url)
result = BeautifulSoup(res.content, 'html.parser')
kospi = result.select_one('#KOSPI_now')
print('현재 코스피 지수는 {}입니다.'.format(kospi))

```

##  플라스크 

사용 tool - https://c9.io  클라우드 방식으로 독립된 가상 머신에 개발환경을 탑재해서 제공해주는

서비스입니다. 

```python
from flask import Flask 
app= Flask(__name__)

@app.route("/")
def hello(): 
    return "hello"
    
    
     $ flask run --host=0.0.0.0 --port=8080
```

## 미세먼지 

```python
import requests
from bs4 import BeautifulSoup
url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=영등포구&dataTerm=MONTH&numOfRows=100&ServiceKey=sfE57qPQ5x1eAXU41ftcyXYJZK5eKEONTGzz%2FdCe069VtqGX4UwcpLZbJhXSayA%2FtauuMhXPXttKeoxuafYWPQ%3D%3D"
#service key의 존재 
response_body = requests.get(url)
result = BeautifulSoup(response_body.content, 'xml')
dust = result('item')[0].pm10Value.text
if(dust>150):
  print("매우나쁨") 
elif(80<dust<150): 
  print("나쁨") 
elif(30<dust<80): 
  print("보통")
else:
  print("좋음")
```

















