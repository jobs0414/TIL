import pandas as pd 
# dictionary 형태로 stock info  저장 

def is_wireless(row): 
    if row == 'mouse' or now == 'keyboard': 
        return True 

    else: 
        return False


def is_year(row):  # 년도만 끊으려고 한다. split 
    
    return row.split('-')[0]





product_list = [
    {'name':'mouse','price':100, 'company': 'AMAZON'}, 
    {'name': 'ssd', 'price':200, 'company': 'GOOGLE'}, 
    {'name': 'keyboard','price':300, 'company':'APPLE'}

]

create_date = [ '2017-09-29', '2017-12-27','2018-01-02']

df = pd.DataFrame(product_list)
df['stock'] = 5 
series = pd.Series(['10%','5%','6%'],index=[0,2,1])
df['D/C'] = series
# df['real_price'] = df['price'] *(1- df['D/C'].str.rstrip('%').astype(float) / 100 
# df['wireless'] = df.company.apply(is_wireless)
df['create date']= create_date
df['year'] = df['create_date'].apply(is_year)
df= df.drop['year']

print(df[df['final price'] >= 200])

print(df)
