# filedemo03.py
try:
    f = open("my_test.txt", "rb")
    text = ""
    line = 1
    
    while True:
        row = f.readline().decode('utf-8')
        if not row: 
            break
        text += str(line) + ":" + row
        line += 1

    f.close()
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
except Exception as ex:
    print("예기치 못한 에러가 발생했습니다.")
else:
    print(text)