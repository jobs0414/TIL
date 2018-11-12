import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm
import numpy as np 

f= open('./day15/ex2.csv')
f.readline()  #first readline skip 
firstline = f.readline().replace('#','').strip().split(',')
secondline = f.readline().replace('#','').strip().split(',')
firstline.extend(secondline)
print(firstline)

loc_dic={}
for index,item in enumerate(firstline): 
    loc_dic[index]= item[:2]

print(loc_dic)
f.close()
exit() 


# data = np.loadtxt('./day15/ex2.csv',dtype=np.int, delimiter=',')
# sale_amount = data[:,2]


# regions = data[:,1]
# happen_event = data[:,2]
# regions_index = range(len(regions))


# font_path = 'C:/Windows/Fonts/batang.ttc'
# fontprop = fm.FontProperties(fname=font_path, size=18)

# flg = plt.figure() 
# ax1 = flg.add_subplot(1,1,1)
# ax1.bar(regions,happen_event, align = 'center', color = 'darkblue')
# ax1.xaxis.set_ticks_position('bottom')
# ax1.yaxis.set_ticks_position('left')
# plt.xticks(regions,happen_event, fontsize='small')


# plt.xlabel('regions') 
# plt.ylabel('happen event') 
# plt.title('regions / happen event') 

# plt.savefig('./day15/traffic.png',dpi =400, bbox_inches= 'tight')




# plt.show()