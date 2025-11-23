def create_dict(filename):  
    """读文件中的单词及释义，以单词为键，其他部分为值创建字典。  
    多个释义间可能是逗号或空格分隔，但单词与第一个释义间至少有一个空格，  
    将读文件并根据空格切分一次，切分结果分别作为键和值创新字典。"""  
    dic = {}                                    # 创建空字典  
    with open(filename, 'r', encoding='utf-8') as data:  
        for x in data:                          # 遍历文件对象  
            x = x.strip().split(maxsplit=1)     # 每行根据空格切分为列表，只切分一次  
            dic.update({x[0].lower(): x[1]})    # 列表的两个元素作为字典的键和值加入字典中  
    return dic


def translate(dic, word):
    """接收两个参数，第一个是读文件创建的字典，第二个参数为要查询的单词，字符串
    根据文件创建的字典，从中查询单词word，
    如果查询单词存在，元组形式返回词与词的释义；
    如果查询不存在，返回'这个词我不明白'
    """
    # 并补充你的代码
    word = word.lower()

    if word in dic:
        value = dic[word]
        return (word, value)
    else:
        return (word, '这个词我不明白')


def translate_word():
    """调用此函数时，先输出提示信息：'请输入查询的单词：'
    用户可循环输入欲翻译的单词，若直接输入回车时，输出'查询结束，正在退出...'。
    输入非空时输出翻译结果
    """
    # 并补充你的代码
    while True:
        word = input('请输入查询的单词：')

        if word == '':
            print('查询结束，正在退出...')
            break
        else:
            print(*translate(word_dic, word))


if __name__ == '__main__':
    file = './dict.txt'           # 表示文件名的字符串，表示位于当前路径下的'dict.txt'文件
    word_dic = create_dict(file)  # 调用函数返回字典类型的数据
    print('载入字典数据成功！')
    translate_word()              # 翻译单词
