
# import math
# #파일 복사 shutil.copy 
# # 파일 이동 shutil.move 
# # 파일 이름변경 shutil.rename
# # 파일 삭제 shutil.remove 

# shutil.copytree('source','target')
# shutil.copytree

# pie=math.pi
# print(pie)

import os 


def listDir(dir): 
    
    files=os.listdir(dir) 
    print("\t\t{0} 디렉토리 내용:".format(dir))
    print("-"*50)
    fileList=[] 
    dirList=[]
    for file in files:
    
        if os.path.isfile(file) == True:
            fileList.append(file) 

        else:

            dirList.append(file) 

    for dirName in dirList: 
        print(dirName)

    print("_----------------")
    for fileName in fileList: 
        print(fileName)



    print(dir)

        #파일? 디렉토리 ? -> isfile(), isdir() 
        #디렉토리 출력, 파일 출력 (이름순)








def main(): 
   
    user_input = input("디렉토리명 ->")
    listDir(user_input)
    # f=open(user_input)
    # dir="c:\\Work\\github\\python"
    # file="c:\\Work\\"

    # print(os.path.isfile(file))
    # print(os.path.isdir(file))

    # listDir(user_input)




main() 




