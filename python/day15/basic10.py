import numpy as np

matrix = np.arange(1, 31).reshape(5, 6)
print(matrix)
print()
print(np.max(matrix))
print(np.sum(matrix, axis=1))
print(np.sum(matrix, axis=0))