# 补充你的代码


n = int(input())
a = [[0 for i in range(n)] for j in range(n)]

x = 0
y = n // 2
cnt = 1
a[x][y] = cnt
cnt += 1

while cnt <= n ** 2:
    nx = x - 1
    ny = y + 1

    if nx < 0:
        nx = n - 1

    if ny >= n:
        ny = 0

    if a[nx][ny] != 0:
        nx = x + 1
        ny = y

    x = nx
    y = ny
    a[x][y] = cnt
    cnt += 1

for line in a:
    print(*line)
