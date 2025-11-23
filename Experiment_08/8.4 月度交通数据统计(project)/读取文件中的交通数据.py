# 请补充你的代码

file = '/data/bigfiles/Monthly_Transportation_Statistics.csv'

n = int(input())

with open(file, 'r', encoding = 'utf-8') as f:
    lines = [line.strip().split(',') for line in f]

for i in range(n):
    print(lines[i])
