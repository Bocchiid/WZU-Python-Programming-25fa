# 以下数据供参考
# q = 5201   # 开采水量
# m = 22     # 含水层厚度
# k = 57.48  # 渗透系数
# a = 6323   # 导压系数
# t = 365    # 开采时间

# 补充你的代码

import math

q = 5201   # 开采水量
m = 22     # 含水层厚度
k = 57.48  # 渗透系数
a = 6323   # 导压系数
t = 365    # 开采时间

r = eval(input())

print(f'预测距离为{r}米时十年间地下水位下降幅度为：', end = '')

for i in range(10):
    s = q / (2 * math.pi * k * m) * math.log(2.25 * a * t / r ** 2)
    t += 365

    print(f'{round(s, 2)}', end = ' ')
