list_a=[52,100,90,80,43]
            
# min_value=min(list_a)
# max_value=max(list_a)

# print("min=", min_value)
# print("max=",max_value)

length = len(list_a)-1 
for i in range(length): 
    for j in range(length-i):
        if list_a[j] < list_a[j+1]: 
            # temp = list_a[j]
            # list_a[j]=list_a[j+1]
            # list_a[j+1]= temp 
            list_a[j], list_a[j+1] = list_a[j+1], list_a[j]
print(list_a[0])
print(list_a[len(list_a)-1])

#알고리즘 로직을 생각하자
#개미수열 로직 구하기. 
