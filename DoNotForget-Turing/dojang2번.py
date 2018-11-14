
#2번 문제 
#어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자. 
#ex) d(91) = 9+ 1 + 91 = 101 
# 이 때 n을 d(n)의 제너레이터라고 한다. 
# 91은 101의 제너레이터  100은 101의 제너레이터 
# 4  5의 제너레이터 
# 제너레이터를 구하는 방법은 자기 자신 각각의 숫자를 더하고 전체 숫자를 더하는 것 
# 1이상 5000보다 작은 셀프 넘버들의 합을 구해보자. 

def d(number): 
    total = number 
    number = str(number)
    for i in number: 
        total = total+int(i)
    return total 


self_number_total =0 
self_number_set =set()

for i in range(1,5000): 
    self_number_set.add(d(i))

for i in range(5000): 
    if not i in self_number_set: 
        self_number_total +=i 

print(self_number_total)

