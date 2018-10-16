import numpy as np

data = np.loadtxt('./day15/ex1.csv', delimiter=',', dtype=np.int)
# 상위 5개
print(data[:5, :]) 
print('-' * 20)
# 배열의 크기
print(data.shape)
print('-' * 20)
# unique 데이터 검사
print(np.unique(data[:, 0]))
print('-' * 20)
# 전국 대상의 가구수 합
print('전국가구수 합:', np.sum(data[:, 1]))
print('-' * 20)
# 가구당 평균 전력사용량의 전국 평균 (소수점 2자리 까지)
print('전국 평균 전력사용량:', round(data[:, 2].mean(), 2))
print('-' * 20)
# 가구당 평균 전력사용량이 400이 넘는 지역과 가구수
print('400초과 지역:',data[data[:, 2] > 400, 0:2])
