import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape, matrix.size)
print(np.array(matrix).reshape(3,2))
print(np.array(matrix).reshape(6,1))
print(np.array(matrix).reshape(1,6))
print(np.array(matrix).reshape(3,1,2))
print(np.array(matrix).flatten())