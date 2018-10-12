# pandas05.py
import pandas as pd

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\pandas_output.csv'

data_frame = pd.read_csv(input_file)

# iloc -> index, 숫자로 데이터 검색
new_data_frame = data_frame.iloc[:, [0, 3]]

new_data_frame.to_csv(output_file, index=False)
print('Pandas Done.')