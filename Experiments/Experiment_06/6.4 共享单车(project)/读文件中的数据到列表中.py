# 补充你的代码


with open('/data/bigfiles/stations.csv', 'r', encoding = 'utf-8') as f:
    lines = f.read().strip().split('\n')

ls = [line.split(',') for line in lines]

n = int(input())

ls = ls[:n]

print(ls)
