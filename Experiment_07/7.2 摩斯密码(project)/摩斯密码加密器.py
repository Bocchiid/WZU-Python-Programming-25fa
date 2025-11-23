def morse_code_encryption(txt):
    """接收明文字符串为参数，返回用摩斯密码加密后的字符串。"""
    char = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '.:,;?=\'/!-_"()$&@'  # 可用于加密的字符
    morse_letter = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morse_digit = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    morse_spec = ['.-.-.-', '---...', '--..--', '-.-.-.', '..- -..', '-...-', '.----.', '-..-.', '-.-.--', '-....-',
                  '..--.-', '.-..-.', '-.--.', '-.--.-', '...-..-', '·-···', '.--.-.', '']  # '.:,;?=\'/!-_"()$&@'的摩斯码
    # 补充你的代码
    ret = ''
    stand = char.index('.')
    txt = txt.lower()

    for c in txt:
        if c.isalpha():
            idx = ord(c) - ord('a')
            ret += morse_letter[idx]
        elif c.isdigit():
            idx = ord(c) - ord('0')
            ret += morse_digit[idx]
        elif c in char:
            shift = char.index(c)
            idx = shift - stand
            ret += morse_spec[idx]
        else:
            ret += c

        ret += ' '

    return ret


if __name__ == '__main__':
    plaintext = input().lower()              # 输入一个字符串并转为小写
    print(morse_code_encryption(plaintext))  # 调用函数，并输出返回值


