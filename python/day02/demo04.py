dic = {
    "a": 100, 
    "b": 200, 
    "c": 300, 
    'd': 400,
    'sum': [10, 20, 30, 40, 50]
}

for key in dic.keys():
    print(key, "=", dic[key])

del dic['sum']
print(dic)
#print(dic['sum'])
if 'sum' in dic:
    print('sum 키가 존재')
else:
    print('sum 키가 존재 X')

