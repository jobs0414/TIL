# basic06.py
from xlrd import open_workbook
import glob, os, sys

input_directory = 'day14'

workbook_count = 0

for input_file in glob.glob(os.path.join(input_directory, '*.xls*')):
    workbook = open_workbook(input_file)
    print('Workbook: {}'.format(os.path.basename(input_file)))
    print('Number of worksheets:', workbook.nsheets)
    for worksheet in workbook.sheets():
        print('Worksheet name:', worksheet.name, \
            '\tRows:', worksheet.nrows, \
            '\tColumns:', worksheet.ncols)
    workbook_count += 1
print('Number of Excel workbooks: {}'.format(workbook_count))