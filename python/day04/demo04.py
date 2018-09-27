# while True:
#     inputData = input("반지름을 입력하세요->")

#     try:
#         num = int(inputData)
#     except Exception as ex:
#         print("type(ex):", type(ex))
#         print("exception:", ex)
#         #print("입력값이 잘못 되었다!")
#         continue
#     else:
#         print("반지름:", num)
#         print("원 둘레:", (3.14 * 2 * num))
#         print("원 넓이:", (3.14 * num * num))
#     finally:
#         print("## 항상실행")    

# print("#### BYE")

# myList = ['100', '90', '80', '70', 'TEST', '60', '50']
# newList = []

# for item in myList:
#     try:
#         int(item)
#         # newList.append(item)
#     except:
#         pass
#     else:
#         newList.append(item)
#     finally:
#         print("항상 실행")

# print(newList) # try ~ except 

score = [85, 80, 60, 100, 70]
while True:
    userData = input("Index를 입력하세요 (0~4)->")
    try:
        num = int(userData)
        if num < 0 or num > 4:
            raise IndexError

        print("{}째 점수는: {}".format(num, score[num]))
    except (ValueError, IndexError):
        print("########### 입력 가능한 범위는 0~4입니다.")
        continue
    except Exception as ex:
        print("########### 예기치 못한 에러가 발생했습니다:", ex)

