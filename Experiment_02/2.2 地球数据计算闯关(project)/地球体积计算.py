# 请补充你的代码

import math

radius = 6371
volumn = 4 / 3 * math.pi * radius ** 3
volumn /= 10000 # 注意单位

print(f'地球体积为{volumn:.4f}万立方千米')
