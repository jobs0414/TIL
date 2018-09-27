# filedemo02.py
f = None
try:
    f = open('my_test.txt', 'rb')
    text = f.read().decode('utf-8')
    print(text)    
except FileNotFoundError:
    print("파일이 존재하지 않습니다.")
finally:
    if not (f is None):
        f.close()
