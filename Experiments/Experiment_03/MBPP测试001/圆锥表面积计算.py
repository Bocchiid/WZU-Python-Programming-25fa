# 请补充你的代码

import math

r, h = map(int, input().split())

l = (r ** 2 + h ** 2) ** 0.5
s = math.pi * r * l + math.pi * r ** 2

print(f'{s:.3f}')
