from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = 'day14/sales_2017.xlsx'
output_file = 'day14/output/3output.xls' # xlsx

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2017_output')

sales_column_index =3 
threshold=2000

with open_workbook(input_file) as workbook:

    data = []
    header= []
    for worksheet in workbook.sheets():
        for row_index in range(1, worksheet.nrows):
            row_info = []
            sale_amount = worksheet.cell_value(row_index, sales_column_index)
            # $ 제거 
            sale_amount = str(sale_amount).replace('$','').replace(',','')
            if sale_amount > threshold:
                
                for col_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, col_index)
                    cell_type = worksheet.cell_type(row_index, col_index)
                    
                    if cell_type == 3: # 날짜데이터형식
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode) # (2017, 1, 1, 0, 0, 0)
                        date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                        row_info.append(date_cell)
                    else:
                        row_info.append(cell_value)
                data.append(row_info) # 조건에 맞는 row의 내용을 추가 
                data.append(row_index[0])

    for row_index, row_info in enumerate(data):
        for col_index, value in enumerate(row_info):
            output_worksheet.write(row_index, col_index, value)

output_workbook.save(output_file)
print('Done.')
