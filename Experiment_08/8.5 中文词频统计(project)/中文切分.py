# 请补充你的代码
import jieba
jieba.setLogLevel(jieba.logging.INFO)

file = '/data/bigfiles/二十大报告.txt'

with open(file, 'r', encoding = 'utf-8') as f:
    text = f.read()

n = int(input())

ls = jieba.lcut(text)

print(ls[:n])
