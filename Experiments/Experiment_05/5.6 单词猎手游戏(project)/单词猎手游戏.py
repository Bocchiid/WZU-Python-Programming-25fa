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

    symbols = '!"#$%&()*+,-.:;[\'][\"]<=>?@[\\]^_‘{|}~/'
    for ch in symbols:
        txt = txt.replace(ch, " ")  # 所有符号替换为空格

    print(f'成功加载{len(txt.split())}个单词')
    # print(txt.split())
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

def get_guessed_word(cover_word, word, letter):
    """接受三个字符串为参数：分别表示正在猜测的遮盖了字母的单词、随机抽取的单词和正在猜测的字母。
    每次猜测后产生一个由猜中字母和下划线与空格组成的字符串，猜中的字母显示出来，未知字母用"_"
    表示，字母间留一个空格。返回每次猜测后由字母和下划线组成的字符串。
    @参数 cover_word：遮盖了字母的单词，字符串类型
    @参数 word：随机抽取的单词，字符串类型
    @参数 letter：正在猜测的字母，字符串类型
    """
    # 补充你的代码
    new_cover_word = ''

    for i in range(len(word)):
        if word[i] == letter:
            new_cover_word += letter
        else:
            new_cover_word += cover_word[i * 2]

        new_cover_word += ' '

    cover_word = new_cover_word
    print(f'当前猜测结果为：{cover_word}')

    return cover_word

def word_guess(word):
    """以随机抽取的秘密单词为参数，参数类型为字符串。
    @参数 word：随机抽取的秘密单词，字符串类型
    先输出一个单词长度的提示信息，产生一个由下划线与空格构成的字符串，每组下划线与空格代表一个字母
    限制用户最多猜测次数为单词长度的2倍
    每次猜测并输入一个字母，调用get_guessed_word()函数对猜测进行处理。
    然后回车换行，并按题目要求进行输出。
    若去除处理后的单词中的空格后得到的单词与传入参数相同，表示已经猜中了秘密单词。
    例如秘密单词为'Tuesday',且用户在6次猜测时猜中了单词中的全部字母，此时输出：
    你太厉害了，居然只用了6次就猜中了单词
    秘密单词是：Tuesday
    '"""
    # 补充你的代码
    length = len(word)
    print(f'单词长度为{length}')

    cover_word = '_ ' * length
    print(cover_word)

    for i in range(2 * length):
        print(f'当前是第{i + 1}次猜测，你还有{2 * length - (i + 1)}次机会')
        
        letter = input('请输入你猜测的字母：')
        cover_word = get_guessed_word(cover_word, word, letter)
        guess_word = cover_word.replace(' ', '')

        if guess_word == word:
            print(f'你太厉害了，居然只用了{i + 1}次就猜中了单词')
            print(f'秘密单词是：{word}')

            break

def judge(txt):
    """接收一个字符串为参数，根据参数值调用不同函数完成任务"""
    test_seed = int(input())
    random.seed(test_seed)
    filename = 'data/gone with the wind.txt'  # 文件名
    wordlist = read_file(filename)
    secretword = secret_word(wordlist)
    if txt == '选词':       # 输出抽中的单词
        # 补充你的代码
        print(secretword)
    elif txt == '模板':     # 输出猜词模板，形如：_ _ _ _ _ _
        # 补充你的代码
        print('_ ' * len(secretword))
    elif txt == '开始填词':
        word_guess(secretword)
    else:
        print('输入错误')

if __name__ == '__main__':
    text = input()
    judge(text)
