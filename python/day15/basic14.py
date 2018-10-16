import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd

f = open('./day15/ex2.csv')
f.readline() #skip
firstlist = f.readline().replace('#', '').strip().split(',')
secondlist = f.readline().replace('#', '').strip().split(',')
firstlist.extend(secondlist)
loc_dic = {}
for index, item in enumerate(firstlist):
    loc_dic[index + 1] = item[:2]
f.close()

def change_value(row):
    return loc_dic[row]

data = np.loadtxt('./day15/ex2.csv', dtype=np.int, delimiter=',')

cdata = data[:, 1] #['AAA', 'BBB', 'CCC', 'DDD', 'EEE']

df = pd.DataFrame(cdata)
customers = df[0].apply(change_value)
sale_amounts = data[:, 2] # [127, 90, 201, 111, 232]

customers_index = range(len(customers))

font_path = 'C:/Windows/Fonts/batang.ttc'
fontprop = fm.FontProperties(fname=font_path, size=18)

flg = plt.figure()
ax1 = flg.add_subplot(1,1,1)
ax1.bar(customers_index, sale_amounts, align='center', color='darkblue')
#ax1.bar(customers, sale_amounts, align='center', color='darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, fontsize='small')

plt.xlabel("사용자 이름", fontproperties=fontprop)
plt.ylabel("판매금액", fontproperties=fontprop)
plt.title("Sale Amount per Customers")

plt.savefig('./day15/output/bar_plt.png', dpi=400, bbox_inches='tight')
plt.show()
