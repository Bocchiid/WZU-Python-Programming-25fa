# 符号常量，用于代替序号访问列表数据
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
NO_KIOSK = 'SMART'


def csv_to_list(csv_file):
    """读文件到列表，返回列表"""
    # 请补充你的代码
    with open(csv_file, 'r', encoding = 'utf-8') as f:
        lines = f.read().strip().split('\n')

    ls = [line.split(',') for line in lines]

    return ls


def is_number(value):
    """判断当前数据是否是数值，返回布尔型。

    >>> is_number('whut211')
    False
    >>> is_number('  211 ')
    True
    >>> is_number('+3.14159')
    True
    """
    # 请补充你的代码
    try:
        float(value)
        return True
    except:
        return False


def clean_data(stations_lst):
    """将数据中的数值字符串转为整数或浮点数：
    若当前数值字符串中的数据是非负整数时，转为int类型；若当前数值字符串中的数据不是非负整数时转为float类型

    >>> d = [['abc', '123', '45.6', 'car', 'Bike']]
    >>> clean_data(d)
    >>> d
    [['abc', 123, 45.6, 'car', 'Bike']]
    >>> d = [['ab2'], ['-123'], ['BIKES', '3.2'], ['3.0', '+4', '-5.0']]
    >>> clean_data(d)
    >>> d
    [['ab2'], [-123], ['BIKES', 3.2], [3.0, 4, -5.0]]
    """
    # 请补充你的代码
    for line in stations_lst:
        for i in range(len(line)):
            it = line[i]

            if is_number(it):
                try:
                    int(it)
                    line[i] = int(it)
                except:
                    line[i] = float(it)


def docks_available_rate(stations_lst, rate):
    """接收站点信息列表和闲置率指标，查询并返回闲置率不低于rater 站点信息的二维列表"""
    # 请补充你的代码
    ls = []
    flag = True

    for line in stations_lst:
        if flag:
            flag = False
            continue

        docks = line[DOCKS_AVAILABLE]
        capacity = line[CAPACITY]

        r = docks / capacity

        if r >= rate:
            ls.append(line)

    return ls


if __name__ == '__main__':
    r = float(input())
    stations_ls = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(stations_ls)
    print(docks_available_rate(stations_ls, r))
