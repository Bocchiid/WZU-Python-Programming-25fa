import string


def top_ten_words_no_excludes(frequency, cnt):
    """接收词频字典，去除常见的冠词、代词、系动词和连接词后，输出出现次数最多的cnt个单词及其出现次数
    需排除的单词如下：
    excludes_words = ['a', 'an', 'the', 'i', 'he', 'she', 'his', 'my', 'we','or', 'is', 'was', 'do',
                      'and', 'at', 'to', 'of', 'it', 'on', 'that', 'her', 'c','in', 'you', 'had',
                      's', 'with', 'for', 't', 'but', 'as', 'not', 'they', 'be', 'were', 'so', 'our',
                      'all', 'would', 'if', 'him', 'from', 'no', 'me', 'could', 'when', 'there',
                      'them', 'about', 'this', 'their', 'up', 'been', 'by', 'out', 'did', 'have']
    """
    ########## Begin ##########
    excludes_words = ['a', 'an', 'the', 'i', 'he', 'she', 'his', 'my', 'we','or', 'is', 'was', 'do', 'and', 'at', 'to', 'of', 'it', 'on', 'that', 'her', 'c','in', 'you', 'had', 's', 'with', 'for', 't', 'but', 'as', 'not', 'they', 'be', 'were', 'so', 'our', 'all', 'would', 'if', 'him', 'from', 'no', 'me', 'could', 'when', 'there', 'them', 'about', 'this', 'their', 'up', 'been', 'by', 'out', 'did', 'have']

    filtered = {key: value for key, value in frequency.items() if key not in excludes_words}

    sorted_dic = sorted(filtered.items(), key = lambda x: -x[1])

    for key, value in sorted_dic[:cnt]:
        print(key, value)
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


def word_frequency(txt):
    """接收去除标点、符号的字符串，统计并返回每个单词出现的次数
    返回值为字典类型，单词为键，对应出现的次数为值"""
    frequency = dict()
    words_list = txt.split()
    for word in words_list:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency


if __name__ == '__main__':
    filename = 'Who Moved My Cheese.txt'  # 文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    frequency_result = word_frequency(content)  # 统计词频
    n = int(input())
    top_ten_words_no_excludes(frequency_result, n)
