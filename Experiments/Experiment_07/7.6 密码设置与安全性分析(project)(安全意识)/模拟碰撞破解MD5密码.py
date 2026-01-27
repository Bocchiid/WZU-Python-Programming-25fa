import hashlib


def make_md5(password: str) -> str:
    """接收一个字符串，用md5加密后转为16进制，返回加密后的字符串"""
    # 补充你的代码
    pass_bytes = bytes(password, 'utf-8')
    pass_md5 = hashlib.md5(pass_bytes).hexdigest()

    return pass_md5


def generate_pass_dic(file: str) -> dict:
    """接收文件名，以其md5加密结果为键、用文件中的密码为值构建字典，返回字典"""
    # 补充你的代码
    dic = {}

    with open(file, 'r', encoding = 'utf-8') as f:
        for line in f:
            line = line.strip()
            line_md5 = make_md5(line)
            dic[line_md5] = line

    return dic


def crack_password(pass_dic: dict, pass_str: str) -> str:
    """接收密码字典和整数n，按加入顺序输出前n项，无返回值"""
    # 补充你的代码
    return pass_dic.get(pass_str, None)

    
if __name__ == '__main__':
    password_str = input()
    filename = '/data/bigfiles/1pass00.txt'
    password_dic_md5 = generate_pass_dic(filename)
    password = crack_password(password_dic_md5, password_str)
    if password:
        print(f'密文{password_str}的明文是{password}')
    else:
        print(f'密文{password_str}的明文未能破解')
