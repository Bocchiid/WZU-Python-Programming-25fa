import string


def count_of_words(txt):
    """接收去除标点、符号的字符串，统计并返回其中单词数量和不重复的单词数量"""
    ########## Begin ##########
    dic = {}

    ls = txt.split()

    for word in ls:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1

    return (len(ls), len(dic))
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
    amount_results = count_of_words(content)
    print('文章共有单词{}个，其中不重复单词{}个'.format(*amount_results))
    
