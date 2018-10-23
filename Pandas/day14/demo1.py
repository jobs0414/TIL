from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = 'day14/sales_2017.xlsx'
output_file = 'day14/output/4output.xls'

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2017_output')



with open_workbook(input_file) as workbook:
    for worksheet in workbook.sheets():
        for row_index in range(1,worksheet.nrows):
            # print(row_index)

            for col_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, col_index)
                cell_type = worksheet.cell_type(row_index, col_index)
                    print(col_index)    