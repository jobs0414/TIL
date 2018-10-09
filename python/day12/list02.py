# list02.py (list -> sort)
from operator import itemgetter

my_list = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678], \
            [578,1,1,290], [461,1,1,290]]

my_sorted_list = sorted(my_list, key=itemgetter(3,0))
print(my_sorted_list)

# a_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
# print('1: {}'.format(a_list))
# a_new_list = a_list[:]
# a_new_list.sort()
# print('2(a_list): {}'.format(a_list))
# print('3(a_new_list): {}'.format(a_new_list))

# my_list = [[1,2,3,4], [4,3,2,1], [2,3,1,4]]
# my_sorted_list = sorted(my_list, key=lambda index_value: index_value[2])
# print('4(my_list): {}'.format(my_sorted_list))

