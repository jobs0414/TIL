# basic09.py
import glob, csv, sys, os

input_path = 'day13\\csv\\'
output_file = 'day13\\csv\\output\\output9.csv'

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        with open(output_file, 'a', newline='') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)

            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                next(filereader)
                for row in filereader:
                    filewriter.writerow(row)
