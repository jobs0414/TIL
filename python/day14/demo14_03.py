import pandas as pd

df = pd.DataFrame([
    {'번호':1, '이름':'a', '국어':100, '영어':100, '나이':15, '합격여부':True},
    {'번호':2, '이름':'b', '국어':90, '영어':80, '나이':16, '합격여부':True},
    {'번호':3, '이름':'c', '국어':80, '영어':70, '나이':15, '합격여부':False},
    {'번호':4, '이름':'d', '국어':70, '영어':60, '나이':14, '합격여부':False},
], columns=['번호', '이름', '국어', '영어', '나이', '합격여부'])

def change_value(row):
    if row == True:
        return '합격'
    else:
        return '불합격'

df['합격여부'] = df['합격여부'].apply(change_value)
df['나이'] = df['나이'] + 1
print(df)
