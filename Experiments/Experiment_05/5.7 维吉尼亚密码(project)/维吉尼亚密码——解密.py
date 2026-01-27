import string

# Get offset array.
def get_offset(key):
    offset = []

    for ch in key:
        if ch.isalpha():
            shift = (ord(ch) - ord('a')) % 26
        elif ch.isdigit():
            shift = (ord(ch) - ord('0')) % 10
        else:
            shift = 0

        offset.append(shift)

    return offset

def vigenere_decrypt(text, key):
    """接收密文字符串和密钥字符串为参数，返回解密后的字符串.
    解密时字母和数字以外的其他字符原样输出。"""
    lower_tab = string.ascii_lowercase    # 小写字母
    upper_tab = string.ascii_uppercase    # 大写字母
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
    # Decrypt plain_text.
    plain_text = ''

    for i in range(len(text)):
        ch = text[i]
        shift = offset[i]

        if ch.isupper():
            ch = chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
        elif ch.islower():
            ch = chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
        elif ch.isdigit():
            ch = chr((ord(ch) - ord('0') - shift) % 10 + ord('0'))

        plain_text += ch

    return plain_text

if __name__ == '__main__':
    secret_key = input()
    cipher_text = input()
    plain_text = vigenere_decrypt(cipher_text, secret_key)
    print(f'解密后得到的明文是{plain_text}')
