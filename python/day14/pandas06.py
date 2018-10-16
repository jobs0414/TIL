# pandas06.py
import pandas as pd

input_file = './day14/sales_2017.xlsx'
output_file = './day14/output/pandas_output.xls'

df = pd.read_excel(input_file, sheetname=None)
row_output = []
for worksheet_name, data_frame in df.items():
    row_output.append(data_frame[data_frame['Sale Amount'].replace('$', '').replace(',','').astype(float) > 2000.0])

new_df = pd.concat(row_output, axis=0, ignore_index=True)
print(new_df)

writer = pd.ExcelWriter(output_file)
new_df.to_excel(writer, sheet_name='sale_amount', index=False)
writer.save()
print("Done.")