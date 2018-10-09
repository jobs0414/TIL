import requests
from bs4 import BeautifulSoup

url = 'http://www.naver.com'
response = requests.get(url)
source = response.text

soup = BeautifulSoup(source, 'html.parser')
top_list = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a')
for top in top_list:
    print(top.text)