import numpy as np 

data = np.loadtxt('./day15/ex2.csv',delimiter=',',dtype=np.float)
print(data)
#1. 상위 3개 발생년도 구분 발생건수 데이터 확인 
print(data[:,:3])
#2.배열의 크기 확인 
print(data.shape)
#3. 중복 지역 존재 여부 확인 (unique)
print(np.unique(data[0]))
#4. 부산의 모든 현황 
print(data[7,:])   #print(data[data[:,1] ==8])
#5. 전국 사고 발생 건수 합계 
print(np.sum(data[:,2]))
#6. 전국에서 증감률이 가장 낮은 곳의 증감률 
print(np.min(data[:,5]))
#7. 사건 발생건수가 400곳 이상인 곳의 작년대비 증감수와 증감률 
        print(data[data[:,2]>400 )]

