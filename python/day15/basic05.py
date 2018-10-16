import numpy as np

a = np.arange(30).reshape(5,6)
print(a)
b = a.reshape(3, 2, 5)
print(b)
# b = np.arange(0, 10, 2)
# print(b)
c = np.zeros(shape=(5,4), dtype=np.int32)
print(c)
d = np.ones(shape=(5,4), dtype=np.int32)
print(d)

e = np.random.randn(4)
print(e)
f = np.random.randn(2, 3)
print(f)