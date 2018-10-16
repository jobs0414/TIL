import numpy as np

matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

vector = np.array([1, 2, 3]).reshape(3,1)
print(matrix + vector)