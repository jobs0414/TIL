import os ,glob 

dir = "C:\\Users\\a\\OneDrive\\python-master\\day06"
os.chdir(dir)
filiter_list=glob.glob('*.txt')
for file in filiter_list: 
    print(file)


# 파일을 불러오르는 함수  /// 재귀함수 사용해서 만들어보기 tree 형태로 .. 
# 흠 파이썬 파일관리 






# files= os.listdir(dir)
# for file in files: 
#     if file. 
#     print(file)