# 请补充你的代码

import math

dlat_01 = float(input('请输入第一个点的纬度（度）：'))
dlon_01 = float(input('请输入第一个点的经度（度）：'))

dlat_02 = float(input('请输入第二个点的纬度（度）：'))
dlon_02 = float(input('请输入第二个点的经度（度）：'))

dlat_01 = math.radians(dlat_01)
dlon_01 = math.radians(dlon_01)

dlat_02 = math.radians(dlat_02)
dlon_02 = math.radians(dlon_02)

r = 6371
d = 2 * r * math.asin(math.sqrt(math.sin((dlat_02 - dlat_01) / 2) ** 2 + math.cos(dlat_01) * math.cos(dlat_02) * math.sin((dlon_02 - dlon_01) / 2) ** 2))

print(f'两点之间的距离为：{d:.2f} 公里')
