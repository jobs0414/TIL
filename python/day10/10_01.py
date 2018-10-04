nums = [ 11, 22, 33,44,55,'hi']
print(nums[0],nums[1],nums[2])


for n in nums: 
    print(n)
print('_'*20)

it = iter(nums) #index -> next() 
while True: 
    try: 
        num = next(it)

    except StopIteration: 
        break

    print(num)


it = iter(nums)
while True: 
    try 
        n
    


# print(next(it))
# print(next(it))
# print(next(it))
