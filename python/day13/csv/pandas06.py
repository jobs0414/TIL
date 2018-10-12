# pandas06.py
import pandas as pd

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\pandas_output.csv'

data_frame = pd.read_csv(input_file)
new_data_frame = data_frame.loc[:, ['Invoice Number', 'Purchase Date']]

new_data_frame.to_csv(output_file, index=False)
print('Pandas Done.')