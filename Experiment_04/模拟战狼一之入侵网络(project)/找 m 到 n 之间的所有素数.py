# 请补充你的代码

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False

    return True

m = int(input())
n = int(input())

for i in range(m, n):
    if is_prime(i):
        print(i, end = ' ')
