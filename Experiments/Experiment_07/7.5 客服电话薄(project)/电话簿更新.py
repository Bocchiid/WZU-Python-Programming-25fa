def read_txt(file: str) -> dict:
    """参数为表示文件名的字符串，读取文件file中的数据，构建包含各公司客服电话的字典，公司名为键，电话号码为值，返回字典。"""
    # 补充你的代码
    with open(file, 'r', encoding = 'utf-8') as f:
        return {key: value for key, value in (line.strip().split(',') for line in f)}


def update_tel_book(company: str, tel_book: dict) -> None:
    """接受公司名与电话簿字典，若公司名存在，调用修改函数，否则调用插入函数
    无返回值"""
    if company in tel_book:
        print(modify_number(company, tel_book))
    else:
        print(add_number(company, tel_book))


def modify_number(company:str, tel_book:dict):
    """接受公司名与电话簿字典，输出提示：'姓名已存在，输入"Y"或"y"修改，其他字符退出'
    输入'Y'后再输入一个新电话号码，将用户的电话号码修改为新值，
    返回'成功修改****电话为*****'；输入其他字符时返回'放弃更新****电话'并退出。
    """
    print(f'{company}电话为{tel_book[company]}')
    print('公司信息已存在，输入"Y"或"y"修改电话号码，其他字符退出')
    # 补充你的代码
    confirm = input()

    if confirm.lower() == 'y':
        print('请输入新的电话号码：')
        new_phone_number = input()
        tel_book[company] = new_phone_number

        return f'成功更新{company}电话为{tel_book[company]}'
    else:
        return f'放弃更新{company}电话'


def add_number(company, tel_book):
    """接受公司名和电话簿字典为参数，用户输入一个电话号码，为字典增加一个以公司名中键，以电话号为值的元素
    返回'成功添加{company}客服电话为{phone_number}'
    """
    print('请输入电话号码：')
    # 补充你的代码
    phone_number = input()
    tel_book[company] = phone_number

    return f'成功添加{company}客服电话为{phone_number}'


if __name__ == '__main__':
    filename = '/data/bigfiles/customer service number.txt'
    phone_dic = read_txt(filename)
    comp = input()                    # 输入要修改信息或新增的公司名
    update_tel_book(comp, phone_dic)  # 更新字典中的数据
