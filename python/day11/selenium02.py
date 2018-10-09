# selenium02.py (facebook login)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth import Auth
from bs4 import BeautifulSoup

auth = Auth('user_info.txt')
user_id = auth.get('user_id')
user_pwd = auth.get('user_pwd')

path = 'C:\\Work\\github\\python\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://www.facebook.com')

element = driver.find_element_by_name('email')
element.send_keys(user_id)
element = driver.find_element_by_name('pass')
element.send_keys(user_pwd)
element.send_keys(Keys.RETURN)

a = driver.find_elements_by_xpath('//*[@id="u_0_a"]/div[1]/div[1]/div/a')
driver.get(a[0].get_attribute('href'))
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
div_list = soup.select('#intro_container_id')
for info in div_list:
    print(info.text)
