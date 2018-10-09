# naver_landnews.py
from bs4 import BeautifulSoup
import requests

page = 1
url = 'https://land.naver.com/news/field.nhn?page=1'
response = requests.get(url)
source = response.text
soup = BeautifulSoup(source, 'html.parser')

maximum = 0
while True: #1232 -> 1233
    page_list = soup.find_all("a", {"class:", "NP=r:" + str(page)})
    if not page_list:
        maximum = page - 1
        break
    page = page + 1
print("전체 " + str(maximum) + " 개의 페이지가 있습니다.")

all_source = ''

for page_number in range(1, maximum + 1):
    url = 'https://land.naver.com/news/field.nhn?page=' + str(page_number)
    response = requests.get(url)
    all_source = all_source + response.text

soup = BeautifulSoup(all_source, 'html.parser')
find_titles = soup.select('#content > div.section_headline > ul > li > dl > dt > a') 
for title in find_titles:
    print(title.text)