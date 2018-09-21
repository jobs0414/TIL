# p = "I like Python better than Java"
# print(len(p))
# print(p.find('e'))
# print(p.rfind('e'))
# print(p.index('e'))
# print(p.count('e'))
# print('a' in p)
# print('b' not in p)
# print(p.isalpha())

# s = "Good morning. my love kim."
# print(s.lower())
# print(s.upper())
# print(s)
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())

# s = "    PYHTON     "
# print(s + ":" + str(len(s)))
# print(s.lstrip() + ":" + str(len(s.lstrip())))
# print(s.rstrip() + ":" + str(len(s.rstrip())))
# print(s.strip() + ":" + str(len(s.strip())))

# s = """ABCDEFG
# APPLE
# BANANA
# ORANGE, GRAPE
# MILK, COFFEE, TEA, WATER"""
# print(s)
# print(s.splitlines())

# s = ".-."
# print(s.join("파이썬프로그래밍"))

# s = """<html>
# <body>
# <h1>HELLO WORLD</h1>
# </body>
# </html>"""
# print(s)
# # '<' -> &lt;  '>' -> &gt;
# print(s.replace('<', '&lt;').replace('>', '&gt;'))

# s = 'PYTHON'
# print(s + ":" + str(len(s)))
# print(s.rjust(10) + ":" + str(len(s.rjust(10))))
# print(s.ljust(10) + ":" + str(len(s.ljust(10))))

# s2 = """ABCDEFG
# APPLE
# BANANA
# ORANGE, GRAPE
# MILK, COFFEE, TEA, WATER"""
# s3 = s2.splitlines()
# for line in s3:
#     a = line.center(20)
#     print(a)

# fmt = "%d년 %d월 %d일"
# for m in range(1, 7):
#     print(fmt % (2018, m, 1))

# s1 = (100, 200, 300)
# print(s1)
# s2 = 100, 200, 300
# print(s2)
# s3 = 100
# print(type(s3))
# s4 = 100,
# print(type(s4))

# a, b = 10, 20
# print(a)
# print(b)

# s = [30, 13500, 2000]
# for price in s:
#     print("가격: %d원" % price)
# print()    
# for price in s:
#     print("가격: %-7d원" % price)

# value = 1234567890
# print(value)
# print("%d" % value)
# print("%20d" % value)

pie = 3.141592
print(pie)
print("%10f" % pie)
print("%10.8f" % pie)
print("%10.5f" % pie)
print("%10.2f" % pie)