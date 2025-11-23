import string
import random
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
    pass_byte = bytes(password, 'utf-8')
    pass_md5 = hashlib.md5(pass_byte).hexdigest()

    return pass_md5

if __name__ == '__main__':
    m = int(input())
    random.seed(m)
    password_str = generate_password(m)
    password_str_md5 = make_md5(password_str)
    # 补充你的代码，输出预期结果
    print(f'产生的密码是：{password_str}，MD5加密结果为{password_str_md5}')
