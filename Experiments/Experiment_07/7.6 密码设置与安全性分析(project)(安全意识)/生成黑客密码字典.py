import string
import hashlib


def generate_password(n: int) -> str:
    """接受一下整数，产生一个n位的密码，返回字符串
    windows密码中支持的特殊字符有："~@_/+:"
    Linux密码中支持的特殊字符有："~@#_^*%/.+:;="
    """
    # 补充你的代码
    char = string.digits + string.ascii_letters + '~@_/+:'

    ls = random.sample(char, n)

    return ''.join(ls)


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


def output(pass_dic: dict, n: int) -> None:
    """接收密码字典和整数n，按加入顺序输出前n项，无返回值"""
    # 补充你的代码
    for key, value in pass_dic.items():
        print(f'密文{key}对应明文密码为{value}')

        n -= 1

        if not n:
            break


if __name__ == '__main__':
    m = int(input())
    filename = '/data/bigfiles/1pass00.txt'
    password_dic_md5 = generate_pass_dic(filename)
    output(password_dic_md5, m)
