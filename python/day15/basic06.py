import numpy as np

# matrix = np.arange(0, 24).reshape(3,8)
# matrix[0,0] = 'a'
matrix = np.full((24), '')
for n in range(matrix.size): # 0 ~ 23
    matrix[n] = chr(n + 97) # 97 ~ 121
print(matrix.reshape(3,8))

matrix2 = np.array([chr(n + 97) for n in range(24)])
print(matrix2.reshape(3,8))


