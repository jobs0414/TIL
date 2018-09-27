import sys, time

if len(sys.argv) != 2: # pyhton 파일명.py 파라미터
    print("날짜를 yyyymmdd로 입력하세요.")
    sys.exit(0)

birth = sys.argv[1] # 파라미터 (날짜))
if (len(birth) != 8 or birth.isnumeric() == False):
    print("날짜 형식이 잘못되었습니다.")
    sys.exit(0)

tm = (int(birth[:4]), int(birth[4:6]), int(birth[6:8]), 0, 0, 0 ,0 ,0 ,0)
ellapse1 = int((time.time() - time.mktime(tm)) / (24 * 60 * 60))
ellapse2 = int(time.time() - time.mktime(tm))
print(ellapse1)
print(ellapse2)



