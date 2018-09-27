# filedemo01.py
f = open('my_test.txt', 'wt')
print(type(f))
text = """설날과 더불어 대한민국에서 
가장 큰 명절 중 하나이자 전일과 다음 날을 
포함한 3일이 법정 공휴일인 날짜만 맞으면 
최대 10일간의 황금연휴가 펼쳐지는 날. 
요즘 들어 추석이 여름인 경우가 늘어나고 있다."""
f.write(text)
f.close()