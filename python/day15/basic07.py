import numpy as np

mabang = np.array([
    [15, 8, 1,24,17],
    [16,14, 7, 5,23],
    [22,20,13, 6, 4],
    [ 3,21,19,12,10],
    [ 9, 2,25,18,11]
])

# col = 0
# sum = 0
# for row in range(mabang.shape[0]):
#     sum += mabang[row, col]
#     col += 1
# print(sum)

print(sum(np.diag(mabang)))

