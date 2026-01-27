# 请补充你的代码

import math

R = 6371
L = 2 * math.pi * R

new_L = L + 1
r = new_L / (2 * math.pi)

difference = r - R
print(f'空隙大小为{difference:.3f}米')

body = 0.1

if (difference > body):
    print('老鼠可以从空隙中钻过')
else:
    print('老鼠无法通过空隙')
