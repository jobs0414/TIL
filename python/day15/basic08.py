import numpy as np

matrix = np.arange(1, 7).reshape(2,3)
print(matrix.sum())
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))
print(matrix.mean())
print(matrix.mean(axis=0))
print(matrix.mean(axis=1))
print(matrix.std())
print(matrix.std(axis=0))
print(matrix.std(axis=1))