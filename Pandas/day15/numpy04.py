
import numpy as np

m = np.array([
    [15,8,1,24,17],
    [16,14,7,5,23],
    [22,20,13,6,4],
    [3,21,19,12,10],
    [9,2,25,18,11]
])
print(m.shape[0])
# print(m.size)
# sum = m[0,0] + m[1,1] + m[2,2] + m[3,3] +m[4,4]
# print("m[{0},{1}]":sum)

# 4행 4열의 대각선 합을 구해라 4행까지 
# 5행 5열의 대각선 합을 구해라 5행까지 
col =0 
sum =0

for row in range(m.shape[0]): 
    sum += m[row,col]
    col +=1 
print(sum)


col = 0 
sum = 0 

for row in range(m.shape[0]): 
    sum+=m[row,col]
    col+=1
print(sum)













