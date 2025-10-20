def csv_to_list(csv_file):
    """读文件到列表，返回列表"""
    # 补充你的代码
    with open(csv_file, 'r', encoding = 'utf-8') as f:
        lines = f.read().strip().split('\n')

    ls = [line.split(',') for line in lines]

    return ls


def is_number(value):
    """判断当前数据是否是数值，返回布尔型。
    以下为文档测试，不会用的同学可以删除
    >>> is_number('whut211')
    False
    >>> is_number('  211 ')
    True
    >>> is_number('+3.14159')
    True
    """
    # 补充你的代码
    try:
        f = float(value)
        return True
    except ValueError:
        return False


def clean_data(data):
    """将数据中的数值字符串转为整数或浮点数：
    若当前数值字符串中的数据是非负整数时，转为int类型；若当前数值字符串中的数据不是非负整数时转为float类型
    以下为文档测试，不会用的同学可以删除
    >>> d = [['abc', '123', '45.6', 'car', 'Bike']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, 'car', 'Bike']]
    >>> d = [['ab2'], ['-123'], ['BIKES', '3.2'], ['3.0', '+4', '-5.0']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], ['BIKES', 3.2], [3.0, 4, -5.0]]
    """
    # 补充你的代码
    for line in data:
        for i in range(len(line)):
            it = line[i]

            if is_number(it):
                try:
                    try_to_int = int(it)
                    line[i] = int(it)
                except ValueError:
                    line[i] = float(it)

    return data


if __name__ == '__main__':
    n = int(input())
    bike_lst = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(bike_lst)
    print(bike_lst[:n])
