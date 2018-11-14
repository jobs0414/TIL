# 각 자릿수의 합을 구할 수 있나요? 
# 사용자가 입력한 양의 정수 각 자리수를 더해 출력하는 프로그램 만들기 
# 5929의 결과는 5+9+2+9 = 25  

total=0 
for i in list(input('number:')): 
    total= total+int(i)
print(total)

num=input("숫자를 입력하세요") 
print(sum(int(n) for n in num))

