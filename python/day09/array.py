import array 

# array 모듈  동일 타입 집합인 배열을 지원 
# 대량 자료를 메모리 낭비 없이 저장 및 고속 엑세스 가능 

my_array = array.array('i',[33,45,80,67,99])
for a in my_array: 
    print(a, end=',')

my_array.append(100)

print()
del my_array[0]
print('my_array[1]=', my_array[1])
print('my_array[2:4]=', my_array[2:4])




list_a = array.array('i',['20','30'])
print(list_a)