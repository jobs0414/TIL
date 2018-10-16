import numpy as np

# a = np.loadtxt('./day15/mabang1.txt')
# print(a[1:-1, 1:-1])

# b = np.loadtxt('./day15/mabang1.txt', dtype=np.int)
# print(b[1:-1, 1:-1])

# c = np.loadtxt('./day15/mabang2.txt', dtype=np.str)
# print(c)

# d = np.loadtxt('./day15/mabang2.txt', dtype=np.int, delimiter=',')
# print(d)

e = np.arange(1, 26).reshape(5, 5)
#np.savetxt('./day15/np_outpu1.txt', e)
# np.savetxt('./day15/np_outpu2.csv', e, delimiter=',')
np.savetxt('./day15/np_outpu3.csv', e, delimiter=',', fmt='%i')
f = np.loadtxt('./day15/np_outpu3.csv', dtype=np.int, delimiter=',')
print(f)