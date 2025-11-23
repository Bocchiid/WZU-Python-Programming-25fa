def read_txt(file: str) -> dict:
    """参数为表示文件名的字符串，读取文件file中的数据，构建包含各公司客服电话的字典，公司名为键，电话号码为值，返回字典。"""
    # 补充你的代码
    with open(file, 'r', encoding = 'utf-8') as f:
        return {key: value for key, value in (line.strip().split(',') for line in f)}


def query_get(company: str, tel_book: dict) -> str:
    """参数 company为表示公司名的字符串，参数 tel_book是字典。
    查询该公司的客服电话号码，返回“用户名：电话号码”的字符串。
    若公司不存在，则在电话号码位置替换为“***不存在”，***表示公司名
    """
    # 补充你的代码
    if company in tel_book:
        return f'{company}:{tel_book[company]}'
    else:
        return f'{company}:{company}客服电话不存在'


if __name__ == '__main__':
    filename = '/data/bigfiles/customer service number.txt'
    phone_dic = read_txt(filename)    # 读文件到字典
    comp = input()                    # 输入公司名
    print(query_get(comp,phone_dic))  # 输出查询结果
