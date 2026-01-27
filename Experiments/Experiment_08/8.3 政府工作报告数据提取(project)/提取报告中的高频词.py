# 补充你的代码
import jieba  # jieba是中文分词库，将中文句子切分成词。
import logging  # 导入模块，用于设置日志级别
jieba.setLogLevel(logging.INFO)    # 关闭jieba日志输出

file_01 = '/data/bigfiles/政府工作报告.txt'
file_02 = 'src/stopword.txt'

with open(file_01, 'r', encoding = 'utf-8') as f:
    ls = jieba.lcut(f.read())

with open(file_02, 'r', encoding = 'utf-8') as f:
    word = jieba.lcut(f.read())

n = int(input())
dic = {}

for item in ls:
    if item not in word and len(item) > 1:
        dic[item] = dic.get(item, 0) + 1

res = [(key, value) for key, value in dic.items()]
res.sort(key = lambda x: -x[1])
res = res[:n]

for key, value in res:
    print(f'{key:<4}{value:>4}')
