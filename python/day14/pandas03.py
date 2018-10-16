# pandas03.py
import pandas as pd

input_file = './day14/sales_2017.xlsx'
output_file = './day14/output/pandas_output.xls'

df = pd.read_excel(input_file, sheetname='january_2017')

filter_date = ['2017-01-24', '2017-01-31']
new_df = df[df['Purchase Date'].isin(filter_date)]

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer, sheet_name='jan_17_output', index=False)
writer.save()
print("Done.")