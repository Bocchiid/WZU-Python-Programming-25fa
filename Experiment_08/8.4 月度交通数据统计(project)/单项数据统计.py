# 请补充你的代码

import pandas as pd
import math

def find_column(key, data_title):
    for i in range(len(data_title)):
        if key == data_title[i]:
            return i


file = '/data/bigfiles/Monthly_Transportation_Statistics.csv'

s = input()

df = pd.read_csv(file)
data_title = df.columns.tolist()
data = df.values.tolist()

idx = find_column(s, data_title)
res = [line[idx] for line in data if math.isnan(line[idx]) is False]
res.sort()
sum_up = sum(res)
ave = sum_up / len(res)

print(f'最小值是{res[0]}，最大值{res[-1]}，平均值{ave:.1f}，中位数值{res[len(res) // 2]}')
