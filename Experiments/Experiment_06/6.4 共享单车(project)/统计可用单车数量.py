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
    # 补充你的代码
    with open(csv_file, 'r', encoding = 'utf-8') as f:
        lines = f.read().strip().split('\n')

    ls = [line.split(',') for line in lines]

    return ls


def is_number(value):
    """判断当前数据是否是数值，返回布尔型。  """
    # 补充你的代码
    try:
        float(value)
        return True
    except:
        return False


def clean_data(stations_lst):
    """将数据中的数值字符串转为整数或浮点数：
    若当前数值字符串中的数据是非负整数时，转为int类型；若当前数值字符串中的数据不是非负整数时转为float类型  """
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


def query_available_bikes(stations_lst):
    """查询带各站点可用单车数量信息，返回各站点可用单车总数量 """
    # 补充你的代码
    sum = 0
    flag = True

    for line in stations_lst:
        if flag:
            flag = False
            continue

        sum += line[BIKES_AVAILABLE]

    return sum


def available_bikes_n(stations_lst, num):
    """查询并输出可用单车数量不少于num的站点信息"""
    # 补充你的代码
    ls = [stations_lst[0]]
    flag = True

    for line in stations_lst:
        if flag:
            flag = False
            continue

        num_bikes_available = line[BIKES_AVAILABLE]

        if num_bikes_available >= num:
            ls.append(line)

    return ls


if __name__ == '__main__':
    stations_ls = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(stations_ls)
    print(query_available_bikes(stations_ls))
    n = int(input())
    print(available_bikes_n(stations_ls, n))

