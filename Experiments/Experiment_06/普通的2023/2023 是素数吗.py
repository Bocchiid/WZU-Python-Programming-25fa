# 请补充你的代码

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    else:
        return True

x = int(input())

if is_prime(x):
    print(f'{x}是素数')
else:
    print(f'{x}不是素数')
