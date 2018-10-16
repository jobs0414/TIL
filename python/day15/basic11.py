import numpy as np

a = np.arange(1, 7).reshape(2,3)
b = np.arange(11, 17).reshape(3,2)
print(a)
print(b)
print(a.dot(b))
print(a.T)