def defac(x):
    factors = []

    for i in range(1, x):
        if x % i == 0:
            factors.append(i)

    return factors

n = int(input())

x = 1
numbers = []

while len(numbers) != n:
    factors = defac(x)
    sum_01 = sum(factors)

    if sum_01 == x:
        numbers.append(x)
        print(f'{x}=', end = '')
        print(*factors, sep = '+')

    x += 1
