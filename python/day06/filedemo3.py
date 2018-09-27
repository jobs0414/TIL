import os,time 

os.chdir("C://")

def listDir(dir): 
    files=os.listdir(dir)
    print("\t\t{0} 디렉토리 내용".format(dir))

    fileList=[] 
    dirList=[]

    #디렉토리 출력, 파일 출력 (이름순)
    
    for file in files:

        if os.path.isfile(file)==True: 
            fileList.append(file)


        else: 
            dirList.append(file)


    for dirName in dirList: 
        print("{0}\t<DIR>\t-\t{1}".format(time.ctime(os.path.getmtime(dirName)),dirName))


    for fileName in fileList:  
        print("{0}\t-\t{1}\t{2}".format(time.ctime(os.path.getmtime(fileName)),os.path.getsize(fileName),fileName))


    print('-'*50)
    print("전체 디렉토리 개수:")
    print("전체 파일 개수:")
    print("전체 파일 용량:")



def main(): 
    user_input=input("디렉토리명: ->")
    listDir(user_input)

    print("파일여부",os.path.isfile(file))
    print("파일크기",os.path.getsize(file))
    print("파일마지막수정일",os.path.getmtime(file))
    print("파일마지막수정일",time.ctime(file))

main() 
