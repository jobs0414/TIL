# basic04.py
import sys, csv
import re

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\output4.csv'

# 001- 
pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)
        filewriter.writerow(header)
        for row in filereader: 
            invoice_number = row[1]
            # match, search, find -> 맞는 패턴만 출력
            if pattern.search(invoice_number):
                filewriter.writerow(row)

print('Done.')