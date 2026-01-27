# 补充你的代码

file = '/data/bigfiles/政府工作报告.txt'

with open(file, 'r', encoding = 'utf-8') as f:
    text = f.read()

n = int(input())
text = text[:n]

print(text)
