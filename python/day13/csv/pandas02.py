# pandas02.py
import pandas as pd

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\pandas_output.csv'

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)

new_data_frmae = data_frame.loc[(data_frame['Supplier Name'].str.contains('Z')) | \
                                    (data_frame['Cost'] > 600.0)]
new_data_frmae.to_csv(output_file, index=False)
print('Pandas Done.')