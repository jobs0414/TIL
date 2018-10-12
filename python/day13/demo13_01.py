my_data = [[1,2,3], [4,5,6], [7,8,9]]
row_to_keep = [row for row in my_data if row[2] > 5]
print('row_to_keep:{}'.format(row_to_keep))

my_data = [(1,2,3), (4,5,6), (7,8,9)]
set_to_tuple1 = {x for x in my_data}
print('set_to_tuple1:{}'.format(set_to_tuple1))
set_to_tuple2 = set(my_data)
print('set_to_tuple2:{}'.format(set_to_tuple2))

my_dic = {'customer1': 7, 'customer2': 10, 'customer3': 15}
my_result = {key: value for key, value in my_dic.items() if value > 10}
print('my_result:{}'.format(my_result))
