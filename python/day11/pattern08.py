import re

# source = 'dowon 010-2222-3333'
# pattern = re.compile('(\w+) \s + ( \d + [-] \d + [-] \d + )')
# m = pattern.findall(source) # findall -> list -> 2 -> group(x)

# print(m.group())
# print(m.group(1))
# print(m.group(2))
# print(m)

# 1. 이메일 패턴이 정확한지 검사 
#      user_id @ domain address -> domain: *.com, *.co.kr, *.net ... 
emails = ['pyhton@example.com', 'pyhton@mail.example.com', 
           'pyhton_a@example.com', 'pyhton-b@example.co.kr', 
           'pyhton_1-@example.net', '@example.com', 
           'pyhton@example', 'dowon.lee@example-com']

pattern = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
for email in emails:
    print(email, '->', (pattern.match(email) != None))

# 2. 휴대전화 검사
#       010, 011
phones = ['010-1111-2222', '010-333-2222', 
            '011-369-5555', '019-456-7890']

pattern2 = re.compile('^(010|011)[-](\d{3,4})[-](\d{4})$')
for phone in phones:
    print(phone, '->', (pattern2.match(phone) != None))