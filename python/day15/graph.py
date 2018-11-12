import matplotlib.pyplot as plt 

customers = ['AAA','BBB','CCC','DDD','EEE']
sale_amount = [127,90,201,111,232]
customers_index = range(len(customers))

flg = plt.figure() 
ax1 = flg.add_subplot(1,1,1)
ax1.bar(customers_index,sale_amount, align = 'center', color = 'darkblue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(customers_index, customers, fontsize='small')

plt.xlabel('customer_name') 
plt.ylabel('sale amount') 
plt.title('sale amount / customer') 

plt.savefig('./day15/bar_plt.png',dpi =400, bbox_inches= 'tight')




plt.show()