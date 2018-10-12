import numpy as np 

matrix = np.array([
    [10,20,30]
    [40,50,60]
    [70,80,90]

])

vector = np.array([1,2,3]).reshape(3,1)


# plus=1
# for m in range(0,3): 
#     vector=np.sum(matrix[m] + plus)
#     plus+=1



print(matrix + vector)