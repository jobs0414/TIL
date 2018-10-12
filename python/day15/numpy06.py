import numpy as np

# matrix1 = np.array([1,2,3])
# matrix2 = np.array([4,5,6])

# print(np.vstack( (matrix1,matrix2) ) )
# print(np.hstack( (matrix1,matrix2) ) )


matrix = np.arange(1,31).reshape(5,6)
print(matrix)
print(np.max(matrix))
print(np.sum(matrix,axis=1))

# print(matrix.mean(axis=0))

a= np.arange(1,7).reshape(2,3)
b= np.arange(11,17).reshape(3,2)
print(a)
print(b)
print(a.dot(b))