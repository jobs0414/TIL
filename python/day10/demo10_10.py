# result = eval("2+3 *5") 
# print(result) 

# a=2 
# print(eval("a * 3"))

# city = [1,2,3]
# forest=[4,5,6]
# for c in city: 
#     for f in forest: 
#         print(f,end=' ')


# exec('value = 10') 
# print(value)
# exec('for i in range(5):print(i,end=',')')

# python = input("코드를 입력하세요")
# exec(python)

code = compile("""
for i in range(10): 
    print(i,end=' ')
print()""",'<string>','exec')


for i in range(10):
    exec(code)
# exec("""
# for i in range(10): 
#     print(i,end=' ')
# print()""")