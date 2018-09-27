import random

cnt = 0
point = 2
while cnt < 10:
    judge = False
    comNum = random.randrange(1, 3)
    while True:
        userNum = int(input("가위(1), 바위(2), 보(3)->"))
        if userNum < 1 or userNum > 3:
            print("다시 입력하세요")
            continue # 가장 인접한 Loop의 조건식으로 이동
        else:
            # 게임 룰 계산 
            if comNum == 1: #가위
                if userNum == 2:  #주먹
                    print("사용자가 이겼습니다.")
                    judge = True
                elif userNum == 3: #보자기
                    print("컴퓨터가 이겼습니다.")
                else:
                    print("비겼습니다.")
                    continue

                break
            elif comNum == 2: #주먹
                if userNum == 3:
                    print("사용자가 이겼습니다.")
                    # try agian? 
                elif userNum == 1:
                    print("컴퓨터가 이겼습니다.")
                else:
                    print("비겼습니다.")
            elif comNum == 3: #보
                if userNum == 1:
                    print("사용자가 이겼습니다.")
                    # try agian? 
                elif userNum == 2:
                    print("컴퓨터가 이겼습니다.")
                else:
                    print("비겼습니다.")
    # ....
    # 게임 종료(judge=True) or 게임 졌을 때(judge=False)
    if judge == True:
        # try again?
        again = input("게임을 계속 할까요?(y/n)")
        if again == 'y' or again == 'Y':
            continue
        else:
            break
    else:
        # game over
        break
# end of while
# display point