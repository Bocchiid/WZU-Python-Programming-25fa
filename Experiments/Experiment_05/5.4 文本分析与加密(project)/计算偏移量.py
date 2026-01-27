import string

# 
def offset_cal(day):
    """用字符串中字符ASCII值的和对26取模为偏移量"""
    # 补充你的代码
    offset = 0

    for ch in day:
        offset += ord(ch)

    offset %= 26

    return offset

if __name__ == '__main__':
    secret_word = input()
    offset_number = offset_cal(secret_word)
    print(offset_number)
