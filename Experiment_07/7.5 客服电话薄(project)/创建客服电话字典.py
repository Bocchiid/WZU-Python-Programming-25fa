def read_txt(file: str) -> dict:
    """参数为表示文件名的字符串，读取文件file中的数据。
    以公司名为键、电话号码为值构建包含各公司客服电话的字典，返回字典。
    """
    # 补充你的代码
    dic = {}

    with open(file, 'r', encoding = 'utf-8') as f:
        for line in f:
            key, value = line.strip().split(',')

            dic[key] = value

    return dic


if __name__ == '__main__':
    filename = '/data/bigfiles/customer service number.txt'
    phone_dic = read_txt(filename)  # 读文件返回字典
    # 补充你的代码输出字典视图
    ls = [(key, value) for key, value in phone_dic.items()]
    print(f'dict_items({ls})')
