import sys 

input_file = './day15/mysql_server_error_log.txt'
output_file = './day15/output/result.csv'

messages = {} # 로그발생날짜 : {로그메세지 : 빈도 }
notes = []  #입력파일 내 모든 로그 메세지

with open(input_file, 'r', newline='') as text_file: 
    for row in text_file: 
        if '[Note]' in row:  # Note가 존재하면 로그 메세지 
            row_list = row.split('',4) # 5개로 분할된 메세지가 저장 
            day = row_list[0].strip() 
            note = row_list[4].strip('\n').strip() 
            if note not in notes: 
                notes.append(note)

            if day not in messages: 
                messages[day] = {} 

            if note not in messages[day]: 
                messages[day][note] = 1 

            else: 
                messages[day][note] += 1 

filewriter = open(output_file, 'w', newline='')
header = ['Date']
header.extend(notes)
header = ','.join(map(str,header)) + '\n'
print(header)
filewriter.write()

for day, day_value in messages.items(): 
    row_of_list = [] 
    row_of_list.append(day)
    for index in range(day_value): 

        pass 


    output = ''
    filewriter.write(output)

filewriter.close() 




