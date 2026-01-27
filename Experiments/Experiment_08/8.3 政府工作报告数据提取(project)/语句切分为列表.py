# 补充你的代码

file = '/data/bigfiles/政府工作报告.txt'
punctuation = ['，', '。', '；'] #中文输入法的逗号，句号及分号

with open(file, 'r', encoding = 'utf-8') as f:
    text = f.read()

for item in punctuation:
    text = text.replace(item, ' ')

n = int(input())

ls = text.split()
ls = ls[:n]

print(ls)
