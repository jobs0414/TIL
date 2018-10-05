# data = """
# 123456-1234567
# 700000-2222222
# 800000-1111111
# """ # -> 123456-*******

# ssn_list = data.split("\n")
# for ssn in ssn_list:
#     converted_data = ''
#     if len(ssn) == 14 and ssn[:6].isdigit() and ssn[7:].isdigit() \
#             and ssn[6:7] == '-':
#         converted_data = ssn[:6] + "-" + "********"
#     print(converted_data)

import re

data = """
123456-1234567
700000-2222222
800000-1111111
"""
pattern = re.compile("(\d{6})[-](\d{7})")
print(pattern.sub("\g<1>-*******", data))
print(pattern.sub("\g<1>-*******",data))


import re 
pattern = re.compile('(\d{6})[-](\d{7})') 
print(pattern.findall(data))
