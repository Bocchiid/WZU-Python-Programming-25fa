# 请补充你的代码

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

x = int(input())

l = 10 ** (x - 1)
r = 10 ** x

for i in range(l, r):
    numbers = denum(i)
    sum_01, sum_02 = get_sum(numbers)

    if i % sum_01 == 0 and i % sum_02 == 0:
        print(i)
