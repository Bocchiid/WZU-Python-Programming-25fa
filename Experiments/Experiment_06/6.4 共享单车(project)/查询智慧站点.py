def csv_to_list(csv_file):
    """读文件到列表，返回列表"""
    # 补充你的代码
    with open(csv_file, 'r', encoding = 'utf-8') as f:
        lines = f.read().strip().split('\n')

    ls = [line.split(',') for line in lines]

    return ls


def is_number(value):
    """判断当前数据是否是数值，返回布尔型。 """
    # 补充你的代码
    try:
        float(value)
        return True
    except:
        return False


def clean_data(stations_lst):
    """将数据中的数值字符串转为整数或浮点数：
    若当前数值字符串中的数据是非负整数时，转为int类型；若当前数值字符串中的数据不是非负整数时转为float类型
    """
    # 补充你的代码
    for line in stations_lst:
        for i in range(len(line)):
            it = line[i]

            if is_number(it):
                try:
                    int(it)
                    line[i] = int(it)
                except:
                    line[i] = float(it)



def is_smart(station):
    """判定当前站点是否是具有智慧功能(名称中有'SMART')，返回布尔值 """
    # 补充你的代码
    key = 'SMART'

    for item in station:
        if is_number(item) is False and key in item:
            return True
    else:
        return False


def query_smart(stations_lst):
    """查询带智慧站点信息，返回站点的二维列表"""
    # 补充你的代码
    ls = []

    for line in stations_lst:
        if is_smart(line):
            ls.append(line)

    return ls


if __name__ == '__main__':
    n = int(input())
    stations_ls = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(stations_ls)
    print(query_smart(stations_ls)[:n])
