# import sys

# print(sys.builtin_module_names)
# for p in sys.path:
#     print(p)
# print("name: {0}".format(__name__))

import calendar

string_weekday = ['월', '화', '수', '목', '금', '토', '일']
day = calendar.weekday(2019, 3, 1)
print(day)
print(string_weekday[day])