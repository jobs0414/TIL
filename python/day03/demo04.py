dic = {}
dic['파이썬'] = 'www.python.org'
dic['마이크로소프트'] = 'www.microsoft.com'
dic['애플'] = 'www.apple.com'

print(dic)
print(type(dic))
print(dic.keys())
print(dic.values())
items = dic.items()
for item in items:
    print(item)
    print(type(item))
print()
for key in dic.keys():
    print(key + "=" + dic[key])
print()    
inputKey = "애플"
#print(inputKey in dic.keys())
if inputKey in dic.keys():
    print("선택한 값은:" + dic[inputKey])
else:    
    print("선택한 값에 해당하는 데이터가 없습니다.")