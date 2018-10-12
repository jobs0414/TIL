# basic05.py
import sys, csv
import re

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\output7.csv'

row_counter = 0
with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        for row in filereader: 
            if row_counter >= 3 and row_counter <= 15:
                filewriter.writerow(row)
            row_counter += 1
print('Done.')