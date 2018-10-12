# basic06.py
import sys, csv
import re

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\output6.csv'

my_columns = ['Invoice Number', 'Purchase Date']
my_columns_index = []

with open(input_file, 'r', newline='') as csv_in_file:
    with open(output_file, 'w', newline='') as csv_out_file:
        filereader = csv.reader(csv_in_file) 
        filewriter = csv.writer(csv_out_file)
        header = next(filereader)   # Supplier Name,Invoice Number,Part Number,Cost,Purchase Date
        for index_value in range(len(header)): # 0, 1, 2, 3, 4
            if header[index_value] in my_columns:
                my_columns_index.append(index_value)
        
        filewriter.writerow(my_columns)

        for row in filereader: 
            row_list_output = []
            for index_value in my_columns_index:
                row_list_output.append(row[index_value])
            filewriter.writerow(row_list_output)
print('Done.')