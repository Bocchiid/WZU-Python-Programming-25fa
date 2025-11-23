def morse_code_decryption(txt):
    """接收密文字符串为参数，返回用摩斯密码解密后的字符串。"""
    char = 'abcdefghijklmnopqrstuvwxyz' + '0123456789' + '.:,;?=\'/!-_"()$&@ '
    morse_letter = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                    "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    morse_digit = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    morse_spec = ['.-.-.-', '---...', '--..--', '-.-.-.', '..- -..', '-...-', '.----.', '-..-.', '-.-.--', '-....-',
                  '..--.-', '.-..-.', '-.--.', '-.--.-', '...-..-', '·-···', '.--.-.', '']
    # 补充你的代码
    ret = ''
    txt = txt.replace('   ', '  ')
    ls = txt.split(' ')

    for item in ls:
        if item in morse_letter:
            idx = morse_letter.index(item)
            ret += char[idx]
        elif item in morse_digit:
            idx = morse_digit.index(item) + char.index('0')
            ret += char[idx]
        elif item in morse_spec:
            idx = morse_spec.index(item) + char.index('.')
            ret += char[idx]
        else:
            ret += item
        
    return ret


if __name__ == '__main__':
    ciphertext = input()                      # 输入一个密文
    print(morse_code_decryption(ciphertext))  # 调用函数，并输出返回值
