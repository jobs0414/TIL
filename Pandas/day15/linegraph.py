import matplotlib.pyplot as plt 
from numpy.random import randn 

plot_data1  = randn(50).cumsum() 
plot_data2  = randn(50).cumsum() 
plot_data3  = randn(50).cumsum() 
plot_data4  = randn(50).cumsum() 

fig = plt.figure() 
ax1 = fig.add_subplot(1,1,1)

#그래프 생성 
ax1.plot(plot_data1, markget = r'o', color=u'blue', linestyle='-', label='Blue Solid delta')
ax1.plot(plot_data2, markget = r'+', color=u'red', linestyle='--', label='Red marine fos')
ax1.plot(plot_data3, markget = r'*', color=u'green', linestyle='-.', label='Green dash pop')
ax1.plot(plot_data4, markget = r's', color=u'orange', linestyle=':', label='Orange Dotted')

ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')

ax1.set_title('Line Plot: Market,Color,Linestyle')
plt.xlabel('Draw')
plt.ylabel("Random Number")
plt.legend(loc='best')
plt.show()


