#  补充你的代码

import math

a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    radius = a * b * c / 4 / area
    area_of_circle = math.pi * radius ** 2

    print(round(area_of_circle, 2))
else:
    print('data error')
