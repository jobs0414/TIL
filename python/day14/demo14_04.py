import pandas as pd

df = pd.read_csv('day14/emp.csv')
# print(df.filter(items=['empno', 'ename', 'job', 'sal']))
# print(df.filter(like='a', axis=1)[0:5]) # 0~4
output_file = 'day14/output/new_output.csv' 
# 1. comm -> NaN => 0 출력 (df.to_csv))
# 2. clerk은 제외하고 출력
df['comm'] = df.comm.fillna(0)
# print(df)
df = df[df['job'] != 'clerk']
df.to_csv(output_file, index=False, na_rep=0)
