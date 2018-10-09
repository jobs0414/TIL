# short_context04.py
my_data = [[1,2,3], [4,5,6], [7,8,9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print('1:{}'.format(rows_to_keep))

my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
set_of_tuple = {x for x in my_data}
print('2:{}'.format(set_of_tuple))
set_of_tuple2 = set(my_data)
print('3:{}'.format(set_of_tuple2))