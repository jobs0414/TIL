import numpy as np 

c=np.loadtxt('./day15/mabang2.txt',dtype=np.str)
print(c)



d= np.loadtxt('./day15/mabang2.txt',dtype=np.int, delimiter=',')
print(d)

e= np.arange(1,26).reshape(5,5)
print(e)
f= np.savetxt('./day15/np_output2.csv',e,delimiter=',')
print('Done.')

## csv 파일 




