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
tempx = x
factors = []
i = x

while x != 1:
    while x % i == 0 and is_prime(i):
        factors.append(i)
        x /= i

    i -= 1

factors.sort(key = lambda x: x)

print(f'{tempx} = ', end = '')
print(*factors, sep = ' × ')
