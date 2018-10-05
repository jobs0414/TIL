import re

source = 'Python is the most powerful language in the world.'

pattern1 = re.compile('^Python') # ^ ~ $
pattern2 = re.compile('^python')

pattern3 = re.compile('world.$') # ^ ~ $
pattern4 = re.compile('world$')

result1 = pattern1.findall(source)
result2 = pattern2.findall(source)
result3 = pattern3.findall(source)
result4 = pattern4.findall(source)
print(result1)
print(result2)
print(result3)
print(result4)