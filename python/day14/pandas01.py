import pandas as pd 

input_file = './day14/sales_2017.xlsx'
output_file = './day14/output/pandas_output.xls'

df = pd.read_excel(input_file, sheetname = 'january_2017')

writer = pd.ExcelWriter(output_file)
df.to_excel(writer,sheet_name='jan_17_output', index = False)
writer.save() 
