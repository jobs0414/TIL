import pandas as pd

# df = pd.DataFrame(data=[[100, 80, 90], [90, 90, 100], [80, 80 , 100]], \
#                     index=['kor', 'math', 'eng'], \
#                     columns=['1번', '2번', '3번'])
# print(df)

# list = [
#     {'name': 'kim', 'age': 10, 'job': 'desinger'},
#     {'name': 'lee', 'age': 20, 'job': 'engineer'},
#     {'name': 'park', 'age': 30, 'job': 'PM'}
# ]
# list = [
#     ['kim', 10, 'desinger'],
#     ['lee', 20, 'engineer'],
#     ['park', 30, 'PM']
# ]
# list = [
#     {'name': ['kim', 'lee', 'park']},
#     {'age': [20, 25, 30]},
#     {'job': ['designer', 'programmer', 'pm']}
# ]
list = [
    ['name', ['kim', 'lee', 'park']],
    ['age', [20, 25, 30]],
    ['job', ['designer', 'programmer', 'pm']]
]

df = pd.DataFrame(list)
print(df.info())
                