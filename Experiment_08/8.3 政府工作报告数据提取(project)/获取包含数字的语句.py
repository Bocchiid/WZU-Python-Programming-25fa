# 补充你的代码

file = '/data/bigfiles/政府工作报告.txt'
punctuation = ['，', '。', '；']  #中文输入法的逗号，句号及分号
number = '0123456789'

with open(file, 'r', encoding = 'utf-8') as f:
    text = f.read()

for item in punctuation:
    text = text.replace(item, ' ')

lines = text.split()

n = int(input())

for line in lines:
    for c in number:
        if c in line:
            print(line)
            n -= 1

            break

    if not n:
        break
