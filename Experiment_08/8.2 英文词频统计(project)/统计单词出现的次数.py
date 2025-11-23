import string


def word_frequency(txt):
    """接收去除标点、符号的字符串，统计并返回每个单词出现的次数
    返回值为字典类型，单词为键，对应出现的次数为值"""
    ########## Begin ##########
    dic = {}

    ls = txt.split()

    for word in ls:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return dic
    ########## End ##########

def top_ten_words(frequency, cnt):
    """接收词频字典，输出出现次数最多的cnt个单词及其出现次数"""
    ########## Begin ##########
    ls = []
    ls = [value for value in frequency.values() if value not in ls]
    ls.sort(reverse = True)
    ls = ls[:cnt]

    res = []

    for key, value in frequency.items():
        if value in ls:
            res.append((key, value))

    res.sort(key = lambda x: -x[1])

    for item in res:
        print(*item)
    ########## End ##########

def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，
    只保留文件中的英文字母和西文符号，过滤掉中文
    所有字符转为小写，
    将其中所有标点、符号替换为空格，返回字符串"""
    with open(file, 'r', encoding='utf-8') as novel:
        txt = novel.read()
    english_only_txt = ''.join(x for x in txt if ord(x) < 256)
    english_only_txt = english_only_txt.lower()
    for character in string.punctuation:
        english_only_txt = english_only_txt.replace(character, ' ')
    return english_only_txt

if __name__ == '__main__':
    filename = 'Who Moved My Cheese.txt'  # 文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    frequency_result = word_frequency(content)  # 统计词频
    n = int(input())
    top_ten_words(frequency_result, n)
    
