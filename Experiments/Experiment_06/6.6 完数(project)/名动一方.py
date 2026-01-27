def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5 + 1)):
        if x % i == 0:
            return False
    else:
        return True

def defac(x):
    factors = []

    for i in range(x):
        factors.append(2 ** i)

    b = 2 ** x - 1

    for i in range(x - 1):
        factors.append(2 ** i * b)

    return factors

n = int(input())

x = 1

while n:
    if is_prime(x) and is_prime(2 ** x - 1):
        n -= 1
        number = (2 ** x - 1) * (2 ** (x - 1))
        factors = defac(x)
        print(f'{number}=', end = '')
        print(*factors, sep = '+')

    x += 1
