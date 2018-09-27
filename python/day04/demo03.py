# score = [88, 95, 70, 100, 99]

# for no, s in enumerate(score, 1):
#     print(str(no) + "번 학생 점수:", s)

# days = ['월','화','수','목','금','토','일']
# food = ['갈비탕', '설농탕', '순대국', '칼국수']
# menu = zip(days, food)
# print(type(menu))
# for d, f in menu:
#     print(d, ' 메뉴:', f)

# score = [45, 98, 72, 50, 94]
# for s in score:
#     if s < 60:
#         print(s)

# score = [45, 90, 72, 50, 85]
# def underD(a):
#     return a < 60
    
# def multiply(a):
#     return a * 2

# for s in filter(lambda a:a<60, score):
#     print(s)

# for s in map(lambda a:a * 2, score):
#     print(s)

# score = [45, 90, 72, 50, 85]
# bonus = [5, 5, 10, 7, 8]

# def total(s, b):
#     return s + b

# for s in map(lambda s,b:s+b, score, bonus):
#     print(s)

import copy

list0 = ['a', 'b']
list1 = [list0, 1, 2]
# list2 = list1.copy()
# list2[0][1] = "c"
# print(list1) -> [[a, c], 1, 2]
# print(list2) -> [[a, c], 1, 2]

list2 = copy.deepcopy(list1)
list2[0][1] = "c"
print(list1)
print(list2)

