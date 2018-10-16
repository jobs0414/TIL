import numpy as np

matrix1 = np.array([1,2,3])
matrix2 = np.array([4,5,6])

print(np.vstack( (matrix1, matrix2) ) )
print(np.hstack( (matrix1, matrix2) ) )