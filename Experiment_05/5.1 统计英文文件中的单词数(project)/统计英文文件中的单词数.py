# 补充你的代码

path = '/data/bigfiles/'

file = input()

with open(path + file, 'r', encoding = 'utf-8') as opened_file:
    text = opened_file.read()

list = [',', '.', '!', '?', "'"]

for mark in list:
    text = text.replace(mark, ' ')

list_01 = text.split()

print(f'共有{len(list_01)}个单词')
