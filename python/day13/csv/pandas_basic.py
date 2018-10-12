# pandas01.py
import pandas as pd
import numpy as np
import os

# df = pd.DataFrame(np.array([[1,2,3], [4,5,6]]))
# print(np.array([[1,2,3], [4,5,6]]))
# print(df.shape)
# print(len(df.index))
# print(list(df.columns))
df = pd.DataFrame({"A": [1,4,7], "B": [2,5,8], "C": [3,6,9]})
print(df)
print(df.iloc[0])
print(df.loc[0])
print(df.ix[0])
print('-' * 10)
df = pd.DataFrame(data=np.array([[1,2,3],[4,5,6],[7,8,9]]), index=[2, 'A', 4], \
                    columns=[51,52,53])
print(df)
print(df.iloc[2])
print(df.loc[2])
print(df.ix[2])
