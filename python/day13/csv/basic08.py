# basic08.py
import glob, csv, sys, os

input_path = 'day13\\csv\\'


file_counter = 0
print(glob.glob(os.path.join(input_path, 'sales_*')))
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    total_row = 1
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader)
        for row in filereader:
            total_row += 1
    print('{0:30s}: {1:d} rows \t{2:d} columns '.format(\
                os.path.basename(input_file), total_row, len(header)))
    file_counter += 1
print("Totol file count: {0:d}".format(file_counter))
