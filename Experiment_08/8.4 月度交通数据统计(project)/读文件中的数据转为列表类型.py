# 请补充你的代码


path = '/data/bigfiles/'
file = input()

with open(path + file, 'r', encoding = 'utf-8') as f:
    lines = [line.strip().split(',') for line in f]

print(lines)
