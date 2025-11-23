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
res = [[line[1].split()[0], line[idx]] for line in data if math.isnan(line[idx]) is False]
res.insert(0, ['Date', s])

print(res)
