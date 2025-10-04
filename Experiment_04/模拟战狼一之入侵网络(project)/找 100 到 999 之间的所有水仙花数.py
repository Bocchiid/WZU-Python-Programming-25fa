# 请补充你的代码

def f(x):
    temp = x

    a = x % 10
    x //= 10
    b = x % 10
    x //= 10
    c = x % 10
    x //= 10

    if a ** 3 + b ** 3 + c ** 3 == temp:
        return True

    return False

for i in range(100, 1000):
    if f(i):
        print(i, end = ' ')
