student = 1
while student <= 5:
    print(student, " 번 학생의 성적 처리")
    student += 1 # for(범위)

num = 1
sum = 0
while num <= 100:
    # 홀수의 합
    if num % 2 == 1:
        sum = sum + num # sum += num

    num = num + 1 # num += 1 
print("1~100까지의 홀수의 합:", sum)

