import string
# 读文件，返回字符串  
def read_file(file):  
    # 补充你的代码
    with open(file, 'r', encoding = 'utf-8') as f:
        return f.read()

# 返回大写字母、小写字母、数字、空格和其他字符的数量  
def classify_char(txt):  
    # 补充你的代码
    upper, lower, digit, space, other = 0, 0, 0, 0, 0

    for ch in txt:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        elif ch.isnumeric():
            digit += 1
        elif ch.isspace():
            space += 1
        else:
            other += 1
    
    return upper, lower, digit, space, other

if __name__ == '__main__':  
    filename = 'mayun.txt'  # 读取的文件名  
    text = read_file(filename)  # text为字符串  
    print(*classify_char(text))
