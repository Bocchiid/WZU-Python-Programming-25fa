# 补充你的代码

pos = [(0, 0), (0, 3), (1, 1), (1, 2), (2, 1), (2, 2), (3, 0), (3, 3)]
n = int(input())
key = n ** 2 + 1

a = [[n * i + j + 1 for j in range(n)] for i in range(n)]

# check init
# for line in a:
#     print(*line)

for i in range(0, n, 4):
    for j in range(0, n, 4):
        for delta_x, delta_y in pos:
            x, y = i + delta_x, j + delta_y
            a[x][y] = key - a[x][y]

for line in a:
    print(*line, sep = '\t', end = '\t\n')
