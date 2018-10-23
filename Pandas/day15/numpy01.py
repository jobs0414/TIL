import numpy as np

# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix)

# print(np.arr1_ndim)
# print(matrix.ndim,matrix.size)

# 배열 인덱싱 
# 기본 List의 인덱싱과 거의 같음 
# array[col]   array[row][col]   array[rank][row][col]

# matrix2 = np.array([ [1,2,3,4,5],
#                     [6,7,8,9,10],
#                     [11,12,13,14,15],
#                     [16,17,18,19,20]
#         ])

# print(matrix2)
# print(matrix2[0,1])
# print(matrix2[0,1:-1])  #앞이 행  뒤가 열 이구나! 


# m = np.array([[0,1,2,3,4],
#             [5,6,7,8,9], 
#             [10,11,12,13,14]]
# )
# print(m)
# print(m[1,2])
# print(m[2,4])
# print(m[1,1:3])
# print(m[2,0:2])
# print(m[1:3,2])
# print(m[0:2,3:5])

import numpy as np 

arr = np.array([1,2,3,4,5,6,7,8,9,10,
                11,12,13,14,15,16,17,18,19,20])

print(arr[arr%3==0])

print(arr[arr%4==1])

print(arr[(arr%3==0) & (arr%4 ==1)])