# basic01.py
import numpy as np

np_arr1 = np.array([1, 2, 3])
print(np_arr1)
np_arr2 = np.array([1, 2.0, '3'])
print(np_arr2)
np_arr3 = np.array([1, 2, 3], float)
print(np_arr3)

print(np_arr1.dtype, np_arr1.shape)
print(np_arr2.dtype, np_arr2.shape)
print(np_arr3.dtype, np_arr3.shape)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)

print(np_arr1.ndim, np_arr1.size)
print(matrix.ndim, matrix.size)
print(10 * '-')
matrix2 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
])
print(matrix2)
print(matrix2[0, 1])
print(matrix2[0, 1:-1])
print(matrix2[:, -2:])
print(matrix2[-2:, -3:])
print(matrix2[1:-1, 1:3])