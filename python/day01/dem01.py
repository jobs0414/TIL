import random

comNum = random.randrange(1, 100)
cnt = 0
while True:
    userNum = int(input("숫자를 입력하세요(1~100)->"))
    cnt += 1
    if userNum < 1 or userNum > 100:
        print("1~100 사이의 숫자를 입력하세요.")
    else:
        if comNum > userNum:
            print("보다 큰 숫자를 입력해 주세요.")
        elif comNum < userNum:    
            print("보다 작은 숫자를 입력해 주세요.")
        else:
            print("맞췄습니다.")
            break # 근접해 있는 Loop 실행 종료

print("=============")
print("COMNUM=", comNum)
print("축하합니다. 총 ", cnt, "번만에 맞추었습니다.")
