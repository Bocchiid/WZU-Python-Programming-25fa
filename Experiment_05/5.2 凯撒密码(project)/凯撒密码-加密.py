import string

def caesar_cipher(text):
    """接收一个字符串为参数，采用字母表和数字中后面第shift个字符代替当前字符的方法
    对字符串中的字母和数字进行替换，实现加密效果，返回值为加密的字符串。
    例如：2019 abc 替换为5shift42 def """
    # 补充你的代码
    shift = 3
    result = ''

    for letter in text:
        if letter.isdigit():
            letter = chr((ord(letter) - ord('0') + shift) % 10 + ord('0'))
        elif letter.isupper():
            letter = chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif letter.islower():
            letter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))

        result += letter

    return result

if __name__ == '__main__':
    plaintext = input()
    print(caesar_cipher(plaintext))
