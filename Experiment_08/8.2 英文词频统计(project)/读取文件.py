import string


def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，
    只保留文件中的英文字母和西文符号，过滤掉中文
    所有字符转为小写，
    将其中所有标点、符号替换为空格，返回字符串"""
    ########## Begin ##########
    content = ''

    with open(file, 'r', encoding = 'utf-8') as f:
        while True:
            c = f.read(1)

            if not c:
                break

            if 0 <= ord(c) <= 255:
                c = c.lower()

                if c in string.punctuation:
                    content += ' '
                else:
                    content += c

    return content
    ########## End ##########

if __name__ == '__main__':
    filename = 'Who Moved My Cheese.txt'  # 文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    n = int(input())
    print(content[:n])
