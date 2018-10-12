import numpy as np 

# matrix = np.array([[1,2,3],[4,5,6]])
# print(matrix)
# print(matrix.shape, matrix.size)
# print(np.array(matrix).reshape(1,6))
# # print(np.array(matrix).reshape(4,2))
# print(np.array(matrix).reshape(3,1,2))

# print(np.array(matrix).flatten())  # 데이터 차수가 변한거 1차원으로 

# a = np.arange(30).reshape(6,5)
# print(a)
# b= np.arange(0,10,2)  # 0~10까지 2배수 
# print(b)

c = np.zeros(shape=(2,4), dtype= np.int32)
print(c)

d = np.ones(shape=(3,5), dtype = np.int32)  #초기값을 지정해서 만들 수 있음. 
print(d)


# e = np.random.randn(4)
# print(e)

# f= np.random.randn(2,3)
# print(f)

g = np.arange(chr(97),chr(110)).reshape(1,1)
print(g)


# m= np.arange().reshape(8,3)  # 8행 3열로 배열하기 
# print(m)













