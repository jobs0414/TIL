# selenium01.py
from selenium import webdriver

path = 'C:\\Work\\github\\python\\chromedriver_win32\\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('http://www.google.com')
# q=blockchain 
search_keyword = driver.find_element_by_name('q')
search_keyword.send_keys('blockchain')
search_keyword.submit()