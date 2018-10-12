# pandas08.py
import pandas as pd
import glob, os, sys

input_path = 'day13\\csv\\'
output_file = 'day13\\csv\\output\\pandas_output.csv'

all_files = glob.glob(os.path.join(input_path, 'sales_*'))

all_data_frames = []

for input_file in all_files:
    data_frame = pd.read_csv(input_file, index_col=None)
    all_data_frames.append(data_frame)
all_data_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
all_data_concat.to_csv(output_file, index = False)
print('Pandas Done.')