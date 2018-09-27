# try:
#     print("네트워크 접속")
#     a = 2 /0 
#     print("....네트워킹 관련 작업....")
#     print("....네트워크 통신 수행....")
# except:
#     print("!! 에러 발생!!")    
# finally:
#     print("접속 해제")

# print("작업 완료")

dic = {'boy':['소년', '남자아이'], 
       'school':['학교', '공부하는 곳'], 
       'book':['책', '정보를 얻을 수 있는 것']}

try:
    print(dic['boy'])
    print(dic['girl'])
except:
    print("찾는 단어가 않습니다.")