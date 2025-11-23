def morse_code_encryption(txt):
    """接收明文字符串为参数，返回用摩斯密码加密后的字符串。"""
    # 补充你的代码
    ls = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    ret = ''
    txt = txt.lower()

    for c in txt:
        if c.isalpha():
            idx = ord(c) - ord('a')
            ret += ls[idx]
        else:
            ret += c
    
    return ret


if __name__ == '__main__':
    plaintext = input().lower()              # 输入一个字符串并转为小写
    print(morse_code_encryption(plaintext))  # 调用函数，并输出返回值
