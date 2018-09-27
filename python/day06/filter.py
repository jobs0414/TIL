import os ,glob 

dir = "C:\\Users\\a\\OneDrive\\python-master\\day06"
os.chdir(dir)
filiter_list=glob.glob('*.txt')
for file in filiter_list: 
    print(file)








# files= os.listdir(dir)


# for file in files: 
#     if file. 
#     print(file)