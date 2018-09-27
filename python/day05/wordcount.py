# import string

# f=open("the_little_prince.txt",'r')
# sentence=f.readlines()
# print(sentence)


# f=open("the_little_prince.txt",'r')
# sentence=f.readlines()

# def printcount(i):
#     global sentence
#     cnt = sentence.count(chr(i))
#     if cnt is not 0:
#         print(chr(i)," : ",cnt)
        
# for i in range(65,91):
#     printcount(i)
# print("-------------------------------------")
# for i in range(97,123):
#     printcount(i)
    
import time 



file=input("Enter the text filename:")
f=open(file,'r')
sentence=f.read()

start=time.time()


def printcount(i):
    global sentence
    cnt = sentence.count(chr(i))
    if cnt is not 0:
        print(chr(i)," : ",cnt)
        
for i in range(65,91):  # 아스키 코드 대문자
    printcount(i)
print("-------------------------------------")
for i in range(97,123):  #아스키 코드 소문자 
    printcount(i)


end=time.time()
print("Elapsed time:", str((end-start)))  