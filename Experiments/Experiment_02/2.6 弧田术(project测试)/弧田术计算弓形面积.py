# 请在下面补充你的代码

b = float(input())
h = float(input())

s = 1 / 2 * (b * h + h ** 2)

print(f'弓形田地面积为{int(s // 240)}亩零{s % 240:.2f}平方步')
