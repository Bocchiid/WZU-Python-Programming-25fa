import string

# Get offset array.
def get_offset(key):
    offset = []

    for ch in key:
        if ch.isalpha():
            shift = ord(ch) - ord('a')
        elif ch.isdigit():
            shift = ord(ch) - ord('0')
        else:
            shift = 0

        offset.append(shift)

    return offset

def vigenere_encryption(text, key):
    """接收明文字符串和密钥字符串为参数，返回加密后的字符串.
    加密时字母和数字以外的其他字符原样输出。
    数字加密时，根据对应的密钥字符在字母表中的偏移量对10取模得到数字的偏移量。
    例如当前数字为1，对应的密钥字母是R,R的偏移量是17，对10取模为7，1 2 3 4 5 6 7 8 9 0 中序号为7的数字是8，加密结果即为8"""
    lower_tab = string.ascii_lowercase  # 小写字母
    upper_tab = string.ascii_uppercase  # 大写字母
    digit_tab = string.digits
    # 补充你的代码
    key = key.lower()
    true_key = ''
    index = 0

    for ch in text:
        if ch.isalpha() or ch.isdigit():
            true_key += key[index]
            index = (index + 1) % len(key)
        else:
            true_key += ch

    # Check true_key.
    # print(true_key)
    # Get offset array.
    offset = get_offset(true_key)
    # Check offset array.
    # print(offset)
    # Get cipher_text
    cipher_text = ''

    for i in range(len(text)):
        ch = text[i]
        shift = offset[i]

        if ch.isupper():
            ch = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        elif ch.isdigit():
            ch = chr((ord(ch) - ord('0') + shift) % 10 + ord('0'))

        cipher_text += ch

    return cipher_text

if __name__ == '__main__':
    secret_key = input()
    plain_text = input()
    plain_to_cipher_text = vigenere_encryption(plain_text, secret_key)
    print(f'加密后得到的密文是{plain_to_cipher_text}')
