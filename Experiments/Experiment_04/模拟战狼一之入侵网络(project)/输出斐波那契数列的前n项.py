# 请补充你的代码

def f(n):
    if not n:
        return 0

    if n == 1:
        return 1

    return f(n - 1) + f(n - 2)

n = int(input())

for i in range(n):
    print(f(i), end = ' ')
