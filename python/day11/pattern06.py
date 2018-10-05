import re

# source = '<li>이도원</li><li>홍길동</li><li>파이썬</li>'
# result = re.match('<li>.*길동</li>', source)
# print(result.group())
#result = re.findall('<li>.*?</li>', source)
#print(result)

pattern = re.compile('a|b')
result1 = pattern.match('abcdefgh')
print(result1.group())
result2 = pattern.findall('abcdefgh')
print(result2)