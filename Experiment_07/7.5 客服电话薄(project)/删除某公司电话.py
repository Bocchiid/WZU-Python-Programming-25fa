def read_txt(file: str) -> dict:
    """参数为表示文件名的字符串，读取文件file中的数据，构建包含各公司客服电话的字典，公司名为键，电话号码为值，返回字典。"""
    # 补充你的代码
    with open(file, 'r', encoding = 'utf-8') as f:
        return {key: value for key, value in (line.strip().split(',') for line in f)}


def del_number(company:str, tel_book:dict)->str:
    """参数 company表示公司名的字符串，参数 tel_book为通讯录字典。
    从字典中删除某公司的信息，删除成功返回提示信息“****电话*****成功删除”
    否则返回“公司名“****”不存在”
    """
    # 补充你的代码
    if company in tel_book:
        value = tel_book[company]
        tel_book.pop(company)
        return f'{company}电话{value}成功删除'
    else:
        return f'公司名“{company}”不存在'
        
        
if __name__ == '__main__':
    filename = '/data/bigfiles/customer service number.txt'
    phone_dic = read_txt(filename)
    comp = input()                      # 输入要删除信息的公司名
    print(del_number(comp, phone_dic))  # 输出删除结果提示信息
 
