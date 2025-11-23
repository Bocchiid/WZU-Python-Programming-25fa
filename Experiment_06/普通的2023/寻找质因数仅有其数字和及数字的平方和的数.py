# 请补充你的代码

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
    i = x

    while x != 1:
        while x % i == 0 and is_prime(i):
            factors.append(i)
            x //= i

        i -= 1

    return factors

def denum(x):
    res = []

    while x:
        r = x % 10
        res.append(r)
        x //= 10

    return res

def get_sum(numbers):
    sum_01 = sum(numbers)
    sum_02 = 0

    for number in numbers:
        sum_02 += number ** 2

    return sum_01, sum_02

def check_sum(sum_01, sum_02, factors):
    flag_01 = False
    flag_02 = False

    for fac in factors:
        if fac == sum_01:
            flag_01 = True
        elif fac == sum_02:
            flag_02 = True
        else:
            return False

    return flag_01 and flag_02

x = int(input())

l = 10 ** (x - 1)
r = 10 ** x

for i in range(l, r):
    factors = defac(i)
    factors.sort(key = lambda x: x)

    numbers = denum(i)
    sum_01, sum_02 = get_sum(numbers)

    if check_sum(sum_01, sum_02, factors):
        print(f'{i} = ', end = '')
        print(*factors, sep = ' × ', end = '')
        print(f'，各位数字的和为{sum_01}, 各位数字的平方和为{sum_02};')
