import string
import random


def generate_password(n: int) -> str:
    """接受一下整数，产生一个n位的密码，返回字符串
    windows密码中支持的特殊字符有："~@_/+:"
    Linux密码中支持的特殊字符有："~@#_^*%/.+:;="
    """
    # 补充你的代码
    char = string.digits + string.ascii_letters + '~@_/+:'
    
    ls = random.sample(char, n)

    return ''.join(ls)


if __name__ == '__main__':
    m = int(input())
    random.seed(m)
    print(generate_password(m))
