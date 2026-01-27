# 补充你的代码

def init_magic_square(a, n, x_delta, y_delta, cnt):
    x = 0 + x_delta
    y = n // 2 + y_delta
    k = 1
    a[x][y] = cnt
    k += 1
    cnt += 1

    while k <= n ** 2:
        nx = x - 1
        ny = y + 1

        if nx < 0 + x_delta:
            nx = n - 1 + x_delta

        if ny >= n + y_delta:
            ny = 0 + y_delta

        if a[nx][ny] != 0:
            nx = x + 1
            ny = y

        x = nx
        y = ny
        a[x][y] = cnt
        k += 1
        cnt += 1

    return n ** 2


def modify_left(a, m):
    limit = m // 2

    for i in range(limit):
        for j in range(limit):
            a[i][j], a[i + m][j] = a[i + m][j], a[i][j]

    for i in range(limit, limit + 1):
        for j in range(limit, limit * 2):
            a[i + m][j], a[i][j] = a[i][j], a[i + m][j]

    for i in range(limit + 1, m):
        for j in range(limit):
            a[i][j], a[i + m][j] = a[i + m][j], a[i][j]


def modify_right(a, m, k):
    x = 0
    y = m + m // 2

    for j in range(y, y - k + 1, -1):
        for i in range(m):
            a[i][j], a[i + m][j] = a[i + m][j], a[i][j]


n = int(input())
k = (n - 2) // 4
m = k * 2 + 1
delta = [(0, 0), (m, m), (0, m), (m, 0)]
a = [[0 for i in range(n)] for j in range(n)]

# check delta
# print(delta)

cnt = 1

for x_delta, y_delta in delta:
    cnt += init_magic_square(a, m, x_delta, y_delta, cnt)

# check init magic square
# for line in a:
#     print(*line)

modify_left(a, m)

# check modify left
# for line in a:
#     print(*line)

modify_right(a, m, k)

# check modify right
# for line in a:
#     print(*line)

for line in a:
    print(*line, sep = '\t', end = '\n')
