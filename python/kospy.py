# https://finance.naver.com/sise/에 요청을 보내서 응답을 받아온다.
import requests
import bs4


url="https://finance.naver.com/sise/"
response = requests.get(url)
# print(response.text)

html = bs4.BeautifulSoup(response.text,"html.parser")
# print(html)

kospi = html.select_one('#KOSPI_now')
print(kospi.text)
