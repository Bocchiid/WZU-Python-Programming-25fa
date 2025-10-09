import string

# 读文件，返回字符串
def read_file(file):    
   with open(file, 'r', encoding='utf-8') as f:      
        return f.read()

def word_list(txt):
    """用空格替换所有符号，切分为列表"""
    for ch in '!"#$%&()*+,-.:;<=>?@[\\]^_’‘{|}~/':
    # 补充你的代码
        txt = txt.replace(ch, ' ')
    
    return txt.split()

def number_of_words(ls):
    """返回单词数量"""
    # 补充你的代码
    return len(ls)

if __name__ == '__main__':
    filename = 'mayun.txt'  # 读取的文件名
    text = read_file(filename)  # text为字符串
    words_list = word_list(text)  # 单词的列表
    words_counts = number_of_words(words_list)
    print(f'共有{words_counts}单词')
