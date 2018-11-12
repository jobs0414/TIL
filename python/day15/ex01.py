import numpy as np 

data = np.loadtxt('./day15/ex1.csv',delimiter=',', dtype = np.int)
#상위 5개 
print(data[:5,:]) 
print('-' * 20)
#배열의 크기 
print(data.shape)
print('-'*20)

#unique 검사 
print(np.unique(data[0]))

#전국 대상의 가구수 합 
print(np.sum(data[:,1]))

#가구당 평균 전력사용량의 전국 평균 (소수점 2자리까지 계산)
print('전국 평균 사용량 계산', round(data[:2].mean(),2))

print('400초과 지역':data[data[:,2]>400], 0:2)



