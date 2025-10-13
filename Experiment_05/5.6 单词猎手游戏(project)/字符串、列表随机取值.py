import random

def read_file(file):
    """接收一个文件名为参数，读取文件中的内容为字符串类型，
    替换字符串中的标点和符号为空格，根据空格将字符串切分为单词为元素的列表，
    返回这个列表。
    @参数 file:文件名，字符串类型
    读取文件前先输出'正在从文件加载单词列表...'
    转为列表后输出输出'成功加载了多少个单词' """
    print('正在从文件加载单词列表...')
    with open(file, 'r', encoding='utf-8') as novel:
        txt = novel.read()
    symbols = '!"#$%&()*+,-.:;[\'][\"]<=>?@[\\]^_‘{|}~/'   #标点、符号 字符串
    # 补充你的代码，将所有符号替换为空格
    for symbol in symbols:
        txt = txt.replace(symbol, ' ')

    print(f'成功加载{len(txt.split())}个单词')
    return txt.split()  # 切分为列表，返回列表

def secret_word(ls):
    """参数为从文件中读取的单词列表，返回值为随机得到的一个单词。
    @参数 ls:单词列表，列表类型
    在测试程序时，可以先预设一个有少数单词的列表，例如随机数种子为19730516时：
    # >>> ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    # >>> secret_word(ls)
    # 'Monday'
    """
    # 补充你的代码
    return random.choice(ls)

if __name__ == '__main__':
    test_seed = int(input())
    random.seed(test_seed)
    filename = 'data/gone with the wind.txt'  # 文件名
    wordlist = read_file(filename)
    secretword = secret_word(wordlist)
    print(secretword)
