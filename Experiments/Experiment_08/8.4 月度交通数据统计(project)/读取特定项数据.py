# 请补充你的代码

import pandas as pd
import math

def find_column(key, data_title):
    for i in range(len(data_title)):
        title = data_title[i]

        if title == key:
            return i

file = '/data/bigfiles/Monthly_Transportation_Statistics.csv'

s = input()

df = pd.read_csv(file)
data_title = df.columns.tolist()
data = df.values.tolist()

idx = find_column(s, data_title)
res = [line[idx] for line in data]

for i in range(len(res)):
    item = res[i]

    if isinstance(item, float) and math.isnan(item):
        res[i] = ''
    elif isinstance(item, float) and item.is_integer():
        res[i] = str(int(item))
    else:
        res[i] = str(item)

res.insert(0, s)
print(res)
