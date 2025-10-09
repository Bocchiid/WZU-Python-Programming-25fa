import string

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

def find_offset(key_text, ciphertext):
    """接收一个单词和一个加密字符串为参数，尝试用[0,25]之间的数为偏移量进行解密。
        如果key_text 在解密后的明文里，则说明解密成功。
    找出偏移量数值并返回这个整数偏移量。"""
    # 补充你的代码
    for i in range(26):
        plain_text = caesar_decrypt(ciphertext, i)

        if key_text in plain_text:
            return i

if __name__ == '__main__':
    key_message = 'question'  # 密文中的已知单词
    cipher_text = 'Yt gj,tw sty yt gj,ymfy nx f vzjxynts.'  # 截获的密文
    secret_key = find_offset(key_message, cipher_text)  # 破解密码，得到密匙
    print(f'密钥是{secret_key}')

    target_text = input()  # 读入新密文，进行解密
    # 'Fyyfhp ts Ujfwq Mfwgtw ts Ijhjrgjw 2, 6496'   #新密文，需要解密
    print(caesar_decrypt(target_text, secret_key))  # 解密，打印明文
