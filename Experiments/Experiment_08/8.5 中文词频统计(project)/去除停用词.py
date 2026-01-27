# 请补充你的代码
import jieba
jieba.setLogLevel(jieba.logging.INFO)

file_01 = '/data/bigfiles/二十大报告.txt'
file_02 = '/data/bigfiles/stopwordsshz.txt'

with open(file_01, 'r', encoding = 'utf-8') as f:
    ls = jieba.lcut(f.read())

with open(file_02, 'r', encoding = 'utf-8') as f:
    word = jieba.lcut(f.read())

dic = {}

n = int(input())

for item in ls:
    if item not in word and len(item) > 1:
        dic[item] = dic.get(item, 0) + 1

res = [(key, value) for key, value in dic.items()]
res.sort(key = lambda x: -x[1])
res = res[:n]

print(res)
