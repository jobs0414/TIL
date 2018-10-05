import re

source = "Dowon Lee 010-2222-3333 edowon0623@gmail.com"

# result1 = re.findall('[a-zA-Z0-9]', source)
result1 = re.findall('\w', source)
# 한 단어
# result2 = re.findall('[a-zA-Z0-9]+', source)
result2 = re.findall('\w+', source)
result3 = re.findall('\W+', source)
# 이메일만 추출
result4 = re.findall('\w+@\w+[.]\w+', source)

print('result1=', result1)
print('result2=', result2)
print('result3=', result3)
print('result4=', result4)