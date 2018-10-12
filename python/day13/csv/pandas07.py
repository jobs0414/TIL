# pandas07.py
import pandas as pd

input_file = 'day13\\csv\\supplier_data_unnecessary_header_footer.csv'
output_file = 'day13\\csv\\output\\pandas_output.csv'

data_frame = pd.read_csv(input_file, header=None)
data_frame = data_frame.drop([0,1,2,16,17,18])
data_frame.columns = data_frame.iloc[0]

new_data_frame = data_frame.reindex(data_frame.index.drop(3))
new_data_frame.to_csv(output_file, index=False)
print('Pandas Done.')