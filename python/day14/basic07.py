# base07.py (all workbooks)
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date
import glob, os, sys

input_folder = 'day14'
output_file = 'day14/output/7output.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('all_data_all_worksheets')

data = []
first_sheet = True
for input_file in glob.glob(os.path.join(input_folder, '*.xls*')):
    with open_workbook(input_file) as workbook:
        for worksheet in workbook.sheets():
            if first_sheet:
                header_row = worksheet.row_values(0)
                data.append(header_row)
                first_sheet = False
            for row_index in range(1, worksheet.nrows):
                row_info = []
                for col_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, col_index)
                    cell_type = worksheet.cell_type(row_index, col_index)

                    if cell_type == 3: # 날짜데이터형식
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode) # (2017, 1, 1, 0, 0, 0)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_info.append(date_cell)
                    else:
                        row_info.append(cell_value)
                data.append(row_info) 
        
for row_index, row_info in enumerate(data):
    for col_index, value in enumerate(row_info):
        output_worksheet.write(row_index, col_index, value)

output_workbook.save(output_file)
print('Done.')