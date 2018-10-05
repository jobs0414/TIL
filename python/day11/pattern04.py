import re

source = "python pytthon pyttthon pyttttttthon pythhhhhon pyhon"
result1 = re.findall('pyt{2}hon', source)
result2 = re.findall('pyt{2,5}hon', source)
result3 = re.findall('pyt{0,}hon', source)
result4 = re.findall('pyt{0,1}hon', source)
result5 = re.findall('pyth{,5}on', source)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)