# tuple03.py
my_tuple = ('x', 'y', 'z')
print('1: {}'.format(my_tuple))
print('2(length): {}'.format(len(my_tuple)))
print('3(index): {}'.format(my_tuple[1]))
long_tuple= my_tuple + my_tuple
print('4(+): {}'.format(long_tuple))

one, two, three = my_tuple
print('5: {0} {1} {2}'.format(one, two, three))
var1 = 'red'
var2 = 'wine'
print('6: {} {}'.format(var1, var2))
var1, var2 = var2, var1
print('7: {} {}'.format(var1, var2))

my_list = [1, 2, 3]
my_tuple = ('x', 'y', 'z')
print('8[1,2,3]->(1,2,3): {}'.format(tuple(my_list)))
print('8(x,y,z)->[x,y,z]: {}'.format(list(my_tuple)))