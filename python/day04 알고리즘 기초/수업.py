dic = {"한상우":'천재' , "김상인":'천재2', "상구": '천재3'}

dic2= { 'boy' : ['남자','소년이라는 뜻' ],
        '절차 지향' : '[나도 몰랑]', 
        '영화뭐볼까?': ['해리포터,매트릭스,터미네이터']
}         # 딕셔너리 형태에 넣어놓은 것 
print(dic)
print(type(dic)) 
print(dic['한상우'])
print(dic['김상인'])
print(dic.get('한상우')) #str 
print(type(dic.get("한상우")))
print(type(dic.get('man')))
# print(dic.get('girl','사전에 존재하지 않는 단어입니다.'))

# print(dic.keys())
# print(dic.values())
# print(dic.items())
# for item in dic.items(): 
# print(repeat,end=' ')
# print(type(repeat))
# print(repeat[0],repeat[1])
#     print(item[0][1])
    
# # dic3={'student':['학생','공부하는 사람'],
# #       'teacher': ['선생님','가르치는 사람'],
# #       'book': ['교과서','공부하기 위한 도구']

# # dic.update(dic3)
# # print(dic)
# # print(len(dic))



# # myList=[['boy','남자아이'],
# #         ['school','공부하는 곳'], 
# #         ['book','공부하기 위한 도구'],
# #         [[1,2]], 'test']]   # dic 형태니까 오류가 난다. key값이 2개로 인식  dic key값은 무조건 1개 


# # dic=dict(myList)    #타입을 변환 시킬 수가 있구나. 리스트 형태로 쓰고 dict 타입으로 변환 가능. 
# # print(type(dic))
# # print(dic)


# # #print(type(myList))
# #print(myList[2][1])


# #딕셔너리로 가져와 보자? 


# # news="""It's obviously very concerning. The potential for some projects to get delayed is very real," said Charlie Riedl, executive director of the Center for Liquefied Natural Gas, a trade group that represents Exxon, Chevron (CVX) and other energy companies.
# # # The shale boom created an excess of natural gas in the United States. In a bid to get rid of the glut, the United States began exporting LNG in 2016 when Houston-based Cheniere (LNG) opened the Sabine Pass terminal in Louisiana. Earlier this year, Dominion Energy (D) opened Cove Point in Maryland, the nation's second export facility .
# # # China is the big elephant in the room. China's appetite for LNG is growing rapidly. And it's on the verge of overtaking Japan as the biggest buyer of LNG in the world."
# # # """

# # {'a':2, 'b':3, 'c':1, 'e':10  ...}
# # alphabet = {} #dict 형태 
# # for char in news: 
# #     if char.isalpha() == False:
# #         continue
# #     char= char.lower()
# #     if char in alphabet:   #True, #False  
# #         alphabet[char]=1   #eye -> {'e':1, 'y':1, } 

# #     else: 
# #         alphabet[char] = alphabet[char]+1   #alphabet[char] = alphabet[char] + 1 

# # for c in range(ord('a'),ord('z')+1):   # range(a~z)까지는 range가 못찾으니까 ord('a)를 써서 range를 잡는다 .
# # #    print(c,chr(c))
# #     print(chr(c),'=', alphabet.get(chr(c),0)) 

 
#  #   alphabet.get(chr(c))







# # print(alphabet)


# # keyList = list(alphabet.keys())
# # keyList.sort() 
# # for key in keyList: 
# #     num=alphabet[key]
# #     print(key,'=',num)

# # print(alphabet['a'])
# # print(alphabet['b'])
# # print(alphabet['c'])






# # 1.검색 x -> 표시 
# # 2. 단어 검출 출력
# # 단어 검출 출력.  =>공백 ->











# # import re  정규식 사용  
# # #리스트로 담아오는 건가  딕셔너리로 가져오는건가 
# # count=news.find("c")
# # print(count)   #wordcount 


# # print(set('dowonlee'))
# # print(set([12,34,56,78,89]))
# # print(set({'boys':'소년','girls':'소녀','grand':'위대한'}))


# # asiaSet = {'korea','china','japan','beti'}
# # #asiaSet.add('usa')
# # #asiaSet.add('korea')
# # #asiaSet.remove('japan')
# # asiaSet.update('singapore','hongkong')*

# # print(asiaSet)

# # enumerate 
# # 순서값에 요소값을 한꺼번에 구하는 내장함수 

# # score= [88,95,70,100,99]
# # for no, s in enumerate(score,1): 
# #     print(str(no) + "번 학생 점수 :", s) 

# # days = ['월','화','수','목','금','토','일']
# # food = ['갈비탕','설농탕','순대국','칼국수']
# # menu = zip(days,food)
# # print(type(menu))

# # for f in menu: 
# #     print(f)
 


# # for s in score: 
# #     if s < 60: 
# #         print(s)


# # score = [45,98,72,50,94]
# # bonus = [5,5,10,7,8]

# # def underD(s): 
# #     return s < 60 

# # def multiply(a): 
# #     return a*2



# # for s in filter(lambda xa:xa<60,score): #람다식 활용법  갓재현! 
# #      print(s)

# # for s in map(lambda a:a*2,score): 
# #     print(s)


# # for s in map(multiply,score): 
# #     print(s)  


# # for n in range(len(score)): 
# #     print(str(n) + "번째 학생", 
# #         score[n], "+", bonus[n],
# #         "=",str(score[n]+bonus[n])) 


# # def total(s,b): 
# #     return s+b 

# # for s in map(total,score,bonus): 
# #     print(s)

# # for s in map(lambda a,b:a+b,score,bonus):
# #     print(s)




# # import copy    

# # list0=['a','b']
# # list1=[list0,1,2]
# # list2= list1.copy() 
# # list2[0][1] = "c"

# # print(list1)

# # list2= copy.deepcopy(list1)
# # list2[0][1] = "c"
# # print(list1)

# # index=5   # user input 
# # list_a=[1,2,3,4,5]
# # print(list_a[1])



# # if index < len(list_a): 
# #     print("error")

# # else: 
# #     print(list_a[index])

# # print(list_a[5])

# # 예외 처리 (Exception Handling)


# # while True:
# #     inputData =input("반지름을 입력해라앗")
# #     try:
# #         num = int(inputData)
# #         print("반지름",num)
# #         print("둘레",(3.14 *2 * num))
# #         print("둘레",(3.14*num*num))

# #     except: 
# #         print("숫자 입력해라 하시용!")
        
# # print("######프로그램 종료######")  



# # for item in myList: 
# #     # if item.isdigit() == True: 
# #     #     newList.append(item)
# #     # else: 
# #     #     print(item,"은(는) 숫자가 아닙니다")
# #     try: 
# #         int(item)
# #         newList.append(item)

# #     except: 
# #         print(item, "은 숫자가 아닙니다요!")
# # print(newList)

# #다르게 







# # myList = ['100','90','80','70','60','50','A']
# # newList=[] 

# # for item in myList: 
# #     # if item.isdigit() == True: 
# #     #     newList.append(item)
# #     # else: 
# #     #     print(item,"은(는) 숫자가 아닙니다")
# #     try: 
# #         int(item)
# #         #newList.append(item)

# #     except: 
# #         print("입력값이 잘못되었다.") 
# #         continue  #돌아간다 루프로 다시 

# #     else: 
# #         print("반지름",num)
# #         print("둘레",(3.14 *2 * num))
# #         print("둘레",(3.14*num*num))
# #     finally: 
# #         print("항상 실행")

# # print(newList) #try ~  except 




# # while True: 
# #     inputData = input("반지름을 입력하세요")

# #     try : 
# #         num = int(inputData)

# #     except Exception as ex: 
# #         print("type(ex):", type(ex))
# #         print("exception:",ex)
# #         continue

# #     else: 
# #         print("반지름",num)
# #         print("둘레",(3.14 *2 * num))
# #         print("둘레",(3.14*num*num))

        
# # score = [85,80,75,70,90]

# # while True:
# #     userData = input("Index를 입력하세요 (0~4)")

# #     try: 
# #         num= int(userData)
# #         if num<0 or num>4:
# #             raise IndexError 
        
# #             # IndexError 
# #         print("{}번째 점수입니다:{}".format(num,score[num]))
        

# #     except ValueError as ex:

# #         print("Type(exception):",type(ex))
# #         print("Exception message:",ex)
# #         print("######## 정수만 입력해주세요")
# #         continue

# #     except IndexError as ex: 

# #         print("Type(exception):",type(ex))
# #         print("Exception message:",ex)
# #         print("######## 입력 가능한 범위는 0~4입니다") 
# #         continue

# #     except Exception as ex: 
        
# #         print("예기치 못한 오류입니다.", ex)   #exception이라는 애는 모든 에러 다 캐치 


# #         # try : 실행할 명령.  예외가 발생할 수 있는 문장 정상 문장 넣어도 됨 
# #         # except : 오류 처리문  except 예외 as 변수 
# #         # 

        
        
# # def calcsum(n): 
# #     if n<0: 
        
# #         return -1 
# #     else: 
  
# #     sum =0 
# #     for i in range(1,n+1): 
# #         sum=sum+i 
# #     return sum  


# # try:  #예외가 발생할 수도 있는 문장 try문장에 넣자!
# #     print('1~10까지의합 :',calcsum(10))
# #     print("1~-5",calcsum(-5))  # return value -> 정수 , ValueError 

# # except Exception as ex:
# #     print("Type 오류 :",type(ex)) 
# #     print("양의 정수를 써주쇼",ex)


# # #조건문으로 처리 

# # result=calcsum(10)
# # if result==-1 
# #     print("양의 정수를 다시 입력하세요")

# # else: 
# #     print("1~10까지의합은 :",result)


# # try: 
# #     print("네트워크 접속")
# #     a=2/0
# #     print("네트워킹 관련 작업")
# #     print("네트워킹 관련 수행")
# #     print("접속해제")

# # except Exception as ex:
# #     print("!!에러 발생 심각한에러!!",ex)

# # finally: 
# #     print("접속 해제")

# # print("작업완료")



# # dic= {'boy':['소년','남자아이'],
# #     'school':['학교','공부하는 곳'],
# #     'book':['책','정보를 얻을 수 있는 곳']
# # }

# # try: 
# #     print(dic['boy'])
# #     print(dic['girl'])

# # except Exception as ex: 
# #     print("사전에", ex, "는없습니다.!! 2019년 9월 21일에 업데이트 예정입니다.")

# # finally:
# #     print("사랑합니다 호갱님 ^^")

# score= 200

# try: 
#     assert score <=100, "점수는 100 이하여야 합니다." 

# except AssertionError as ex: 
#     print(ex)

# else:
#     print(score)




































