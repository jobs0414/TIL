#filedemo_01.py 

# rows=f.readlines() 
# for row in rows: 
#     print(row,end=' :')
# f.close()

#한줄씩 출력하는 방법. 

# for line in f: 
#     print(line,end=' ')
# f.close() 

# f.seek(12,0)
# text=f.read() 
# f.close() 
# print(text)


f=open("my_test.txt", 'r+')
f.write("\n\n파이썬 파일읽기 쓰기 예제")
text=f.read()
f.seek(0) #파일 위치를 첫번째로 가져온다. 
 
f.close() 
print(text)





# with open("my_test.txt",'rt') as f: 
#     text=f.read() 

print(text)

## 파일 복사 
# 0. 실행시 [원본 파일] [복사될 파일명]

# 1. 읽기 
# read() readlines() 
# 2. 쓰기 
# write() 

# f=open("my_test.txt",'at')
# file=f.readlines()

# file.write("file copy 입니다.")
# print("file newfile : ")












