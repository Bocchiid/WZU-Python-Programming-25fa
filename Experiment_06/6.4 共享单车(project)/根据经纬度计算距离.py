# 补充你的代码
# 导入数学模块
# 导入随机数模块
import math
import random


def csv_to_list(csv_file):
    """读文件到列表，返回列表"""
    # 补充你的代码
    with open(csv_file, 'r', encoding = 'utf-8') as f:
        lines = f.read().strip().split('\n')

    ls = [line.split(',') for line in lines]

    return ls


def is_number(value):
    """判断当前数据是否是数值，返回布尔型。
    以下为文档测试，不会用的同学可删除
    >>> is_number('whut211')
    False
    >>> is_number('  211 ')
    True
    >>> is_number('+3.14159')
    True
    """
    # 补充你的代码
    try:
        float(value)
        return True
    except:
        return False


def clean_data(data):
    """将数据中的数值字符串转为整数或浮点数：
    若当前数值字符串中的数据是非负整数时，转为int类型；若当前数值字符串中的数据不是非负整数时转为float类型
    以下为文档测试，不会用的同学可删除
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
                    int(it)
                    line[i] = int(it)
                except:
                    line[i] = float(it)


def get_location(lsm, lsn):
    """获取随机抽取的两个站点的经纬度（[纬度, 经度]）
    返回形如([43.681991, -79.329455], [43.6574766, -79.373446])的元组
    """
    # 补充你的代码
    return ([lsm[2], lsm[3]], [lsn[2], lsn[3]])


def get_distance(lon_and_lat):
    """接收两个点的经纬度，计算并返回两点间距离"""
    # 补充你的代码
    r = 6371.004
    phi_01 = math.radians(lon_and_lat[0][0])
    phi_02 = math.radians(lon_and_lat[1][0])
    lambda_01 = math.radians(lon_and_lat[0][1])
    lambda_02 = math.radians(lon_and_lat[1][1])

    d = 2 * r * math.asin(math.sqrt(math.sin((phi_02 - phi_01) / 2) ** 2 + math.cos(phi_01) * math.cos(phi_02) * math.sin((lambda_02 - lambda_01) / 2) ** 2))

    return d
    

if __name__ == '__main__':
    s = int(input())  # 输入随机数种子
    # 补充语句设置随机数种子
    random.seed(s)
    
    bike_lst = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(bike_lst)
    m, n = random.randint(1, len(bike_lst)), random.randint(1, len(bike_lst))
    longitude_and_latitude = get_location(bike_lst[m], bike_lst[n])  # 抽取站点的经纬度
    # longitude_and_latitude = ([-122.423246, 37.779388], [-117.220406, 32.719464])  # 测试数据，结果应为642.185478152公里
    dist_of_mn = get_distance(longitude_and_latitude)
    print(longitude_and_latitude)
    print(f'两个站点间距离为{dist_of_mn:.3f}公里')
