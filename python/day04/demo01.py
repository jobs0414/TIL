dic = {'boy':['소년', '남자아이'], 
       'school':['학교', '공부하는 곳'], 
       'book':['책', '정보를 얻을 수 있는 것']}

# dic2 = {'student':['학생', '공부하는 사람'],
#         'teacher':['선생님', '가르치는 사람'],
#         'book':['교과서', '공부하기 위한 도구']}

# dic.update(dic2)
# print(dic)
# print(len(dic))

print(type(dic.keys()))
print(dic.values())
# print(dic.items()) # dictionary -> tuple 
# print(type(dic.items()))
# for item in dic.items():
#     print(item) # tuple 
#     print(item[0], item[1])
#     print(item[0], item[1][0], item[1][1])

# print(dic)
# print(type(dic))
# # print(dic['boy']) # dictread
# # print(dic['girl'])
# print(dic.get('girl'))
# print(dic.get('girl', '사전에 존재하지 않는 단어입니다.'))

myList = [['boy', '남자아이'], 
          ['school', '공부하는 곳'],
          ['book', '공부하기 위한 도구'],
          [123, '숫자입니다.'],
          [1, ['tets',123]]]
dic = dict(myList)
print(type(dic))
print(dic)
# print(type(myList))
# print(myList[2][1])