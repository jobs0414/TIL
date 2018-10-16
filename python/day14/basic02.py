from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = 'day14/sales_2017.xlsx'
output_file = 'day14/output/2output.xls' # xlsx

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2017_output')

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2017')
    # sheet -> rows ? columns ? 
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            if worksheet.cell_type(row_index, col_index) == 3: # 날짜데이터형식
                date_cell = xldate_as_tuple(worksheet.cell_value\
                                (row_index, col_index), workbook.datemode) # (2017, 1, 1, 0, 0, 0)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                output_worksheet.write(row_index, col_index, \
                                        worksheet.cell_value(row_index, col_index))

output_workbook.save(output_file)
print('Done.')