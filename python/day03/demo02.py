# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(s)
# print(s[2])
# s[2] = 50
# print(s)
# s[2:5] = [10, 20, 30]
# print(s)
# s[6:8] = [100, 200, 300, 400, 500]
# print(s)

# s = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# print(s)
# for outerEl in s:
#     #print(outerEl) # outerEl = list
#     print("LEN=" + str(len(outerEl)))
#     for innerEL in outerEl:
#         print(innerEL, end='\t')
#     print()    

# nums = [1, 2, 3, 4]
# nums[2:2] = [90, 91, 92]
# print(nums)
# print(str(len(nums)))

# nums = [1, 2, 3, 4]
# nums[2] = [90, 91, 92]
# print(nums)
# print(str(len(nums)))

# score = [88, 95, 100, 70, 99, 80, 50]
# perfect = score.index(100) + 1
# print("만점 받은 학생은 %d번입니다." % perfect)
# perfectNum = score.count(100)
# print("만점 받은 학생은 {}명 입니다.".format(perfectNum))

# score.sort()
# print(score)
# score.reverse()
# print(score)

# words = ['apple', 'banana', 'orange', 'melon', 'grape', 'coffee', 
#          'tea', 'black-tea']
# words.sort()
# print(words)
# words.sort(reverse=True)
# print(words)
# words.sort(key=len)
# print(words)

sungjuk = [('HONG', 100, 90), ('KIM', 80, 70), ('LEE', 95, 55)]
print(sungjuk)
sungjuk.sort(key = lambda element : element[1])
print(sungjuk)