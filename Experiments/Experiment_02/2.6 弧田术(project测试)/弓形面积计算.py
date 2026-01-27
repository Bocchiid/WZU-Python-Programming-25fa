# 请在下面补充你的代码

import math

AB = float(input())
CD = float(input())

s_1 = 1 / 2 * (AB * CD + CD ** 2)

AD = AB / 2
OA = (AD ** 2 + CD ** 2) / (2 * CD)

AOB = 2 * math.asin(AD / OA)

sector = AOB / (2 * math.pi) * math.pi * OA ** 2
triangle = 1 / 2 * OA ** 2 * math.sin(AOB)

arch = sector - triangle

print(f'弧田法计算弓形田地面积为{int(s_1 // 240)}亩零{s_1 % 240:.2f}平方步')
print(f'现代方法计算弓形田地面积为{int(arch // 240)}亩零{arch % 240:.2f}平方步')
