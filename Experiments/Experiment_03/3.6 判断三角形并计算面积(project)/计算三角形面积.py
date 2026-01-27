#  补充你的代码

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    print(round(area, 2))
else:
    print('data error')
