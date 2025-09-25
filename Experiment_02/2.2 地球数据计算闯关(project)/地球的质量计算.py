# 请补充你的代码

import math

radius = 6371
volumn = 4 / 3 * math.pi * radius ** 3

density = 5507.85

weight_01 = volumn * 1000 ** 3 * density / 10000 / 100000000 / 1000
weight_02 = volumn * 1000 ** 3 * density

print(f'地球质量约为{weight_01:.1f}万亿吨')
print(f'地球质量约为{weight_02:e}千克')
