# 请补充你的代码

def is_factor(a, b):
    return a % b == 0

n = int(input())

for i in range(1, n + 1):
    if is_factor(n, i):
        print(i, end = ' ')
