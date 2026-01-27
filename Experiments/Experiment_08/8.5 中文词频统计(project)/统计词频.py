# 请补充你的代码
import jieba
jieba.setLogLevel(jieba.logging.INFO)

file = '/data/bigfiles/二十大报告.txt'

with open(file, 'r', encoding = 'utf-8') as f:
    text = f.read()

ls = jieba.lcut(text)
dic = {}

n = int(input())

for item in ls:
    dic[item] = dic.get(item, 0) + 1

res = [(key, value) for key, value in dic.items()]
res.sort(key = lambda x: -x[1])
res = res[:n]

print(res)
