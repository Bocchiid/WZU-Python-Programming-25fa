import string

def judge(txt):
    """接收一个字符串为参数，如果参数值为“加密”,要求用户输入一个要加密的文件名，
    再输入一个单词做为密钥发生器，用于计算偏移量，对文件中的内容进行加密并输出。
    如果参数值为“解密”,要求用户输入一个要解密的文件名，再输入一个单词做为匹配词，
    用于破解偏移量，输出解密后的文本。若为其他输入，输出'输入错误'。"""
    # 补充你的代码
    if txt == '加密':
        file = input()
        key_word = input()

        text = read_txt(file)
        offset = cal_offset(key_word)
        cipher_text = caesar_cipher(text, offset)

        print(cipher_text)
    elif txt == '解密':
        file = input()
        key_word = input()

        text = read_txt(file)
        offset = find_offset(key_word, text)
        decrypt_text = caesar_decrypt(text, offset)

        print(decrypt_text)
    else:
        print('输入错误')

def read_txt(file):
    """接收文件名为参数，读取文件中的内容为一个字符串，返回这个字符串。"""
    with open(file, 'r') as temp:
        return temp.read()

def caesar_cipher(text, offset):
    """接收一个字符串为参数，采用字母表和数字中后面第offset个字符代替当前字符的方法
    对字符串中的字母和数字进行替换，实现加密效果，返回值为加密的字符串。
    例如：2019 abc 替换为5342 def """
    # 补充你的代码
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits

    before = lower[offset:] + lower[:offset] + upper[offset:] + upper[:offset] + digit[offset:] + digit[:offset]
    after = string.ascii_letters + digit

    table = str.maketrans(after, before)
    cipher_text = text.translate(table)

    return cipher_text

def caesar_decrypt(text, offset):
    """接收一个加密的字符串text和一个整数offset为参数，采用字母表和数字中前面第offset个字符
    代替当前字符的方法对字符串中的字母和数字进行替换，实现解密效果，返回值为解密的字符串。"""
    # 补充你的代码
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits

    before = string.ascii_letters + digit
    after = lower[offset:] + lower[:offset] + upper[offset:] + upper[:offset] + digit[offset:] + digit[:offset]

    table = str.maketrans(after, before)
    decrypt_text = text.translate(table)

    return decrypt_text

def cal_offset(key_word):
    """接收一个单词为参数，计算这个单词的每个字母的ASCII值的和，
    再对9取模，结果作为偏移量offset，返回这个偏移量。"""
    # 补充你的代码
    offset = 0

    for letter in key_word:
        offset += ord(letter)

    offset %= 9

    return offset

def find_offset(key_text, ciphertext):
    """接收一个明文单词和一个加密字符串为参数，尝试用[0,8]之间的数为偏移量进行解密。
    若解密结果中包含这个明文单词，说明当前正在尝试的偏移量就是加密时所用偏移量，返回
    这个整数偏移量。
    """
    # 补充你的代码
    for i in range(9):
        plain_text = caesar_decrypt(ciphertext, i)

        if key_text in plain_text:
            return i

if __name__ == '__main__':
    task = input()
    judge(task)
