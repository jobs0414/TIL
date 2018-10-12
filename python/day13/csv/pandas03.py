# pandas03.py
import pandas as pd

input_file = 'day13\\csv\\supplier_data.csv'
output_file = 'day13\\csv\\output\\pandas_output.csv'

data_frame = pd.read_csv(input_file)
filter_date = ['1/20/14', '1/30/14']
notin_filter_date = ['2002-03-14']

# filtered_df = ~data_frame['Purchase Date'].isin(filter_date)
# new_data_frame = data_frame.loc[~data_frame['Purchase Date'].\
#                                     isin(notin_filter_date), :] # [row:column]
new_data_frame = data_frame.loc[~data_frame['Purchase Date'].\
                                    str.contains('2002'), :] # [row:column]

new_data_frame.to_csv(output_file, index=False)
print('Pandas Done.')