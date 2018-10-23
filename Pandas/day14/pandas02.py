import pandas as pd 
import re 

input_file = './day14/sales_2017.xlsx'
output_file = './day14/output/pandas_output.xls'

df = pd.read_excel(input_file, sheetname =None)
row_output=[]
for worksheet_name, data_frame in df.items(): 
    row_output.append(data_frame[data_frame['Sale Amount'].replace('$','').replace(',','').astype(float) > 2000.0])

new_df = pd.concat(row_output, axis=0, ignore_index=True)
# name = re.compile[r'J+']

# new_df = df[df['Customer Name'].str.startswith('J')]
# new_df = df.iloc[:,[1,2,3,4]]
# print(new_df)
#iloc (순서)  loc(이름)
print(new_df)

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer,sheet_name='sale_amount', index = False)
writer.save() 
print("성공")