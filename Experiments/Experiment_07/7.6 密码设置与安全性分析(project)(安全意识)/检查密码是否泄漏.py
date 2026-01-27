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


def read_txt() -> dict:
    """无参数，读取多个文件，将其中的密码用md5加密后存于字典"""
    path = '/data/bigfiles/'
    file_ls = ['1pass00.txt', '1pass01.txt', '1pass02.txt', '1pass03.txt']
    # 补充你的代码
    dic = {}

    for file in file_ls:
        dic.update(generate_pass_dic(path + file))

    return dic


def check_pass(leaked_pass_dic:dict, pass_str_md5: str):
    """检查用户的密码是否在泄漏密码库中存在，存在时返回明文，不存在时返回None"""
    # 补充你的代码
    return leaked_pass_dic.get(pass_str_md5, None)


if __name__ == '__main__':
    password_str = input()
    password_str_md5 = make_md5(password_str)
    leaked_pass_dict = read_txt()
    result = check_pass(leaked_pass_dict, password_str_md5)
    if result:
        print(f'你的密码是{result}，你的密码在泄漏密码字典中')
    else:
        print('你的密码安全')
