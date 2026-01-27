# 请补充你的代码

import math

radius = 6371
area = 4 * math.pi * radius**2
area /= 10000 # 注意单位

print(f'地球表面积为{area:.4f}万平方千米')
