from xlrd import open_workbook 

input_file = 'day14/sales_2017.xslx'
workbook = open_workbook(input_file)
print('Numbers of worksheets:', workbook.nsheets)

for worksheet in workbook.sheets(): 
    print('worksheet name:',worksheet.name, \ 
        '\tRows:',worksheet.nrows, \ 
        '\tColumns:', worksheet.ncols) 
    
    ) 