def create_dict(filename):
    """接收表示文件名的字符串参数，读文件中的单词及释义，以单词为键，其他部分为值创建字典。
    多个释义间可能是逗号或空格分隔，但单词与第一个释义间至少有一个空格，
    将文件每一行根据空格切分一次，切分结果分别作为键和值创新字典。
    返回字典。
    """
    #####################Begin#####################################
    dict = {}

    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            line = line.strip()

            key, value = line.split(' ', 1)

            dict[key] = value

    return dict
    #####################End#####################################


if __name__ == '__main__':
    file = './dict.txt'           # 表示文件名的字符串，表示位于当前路径下的'dict.txt'文件
    word_dic = create_dict(file)  # 调用函数返回字典类型的数据
    print(len(word_dic))
