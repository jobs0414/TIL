import re

source = "py pyt pyth pytho python picham"
result = re.findall('py?', source)
print('result=', result)