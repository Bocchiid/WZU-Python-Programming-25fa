from typing import List, TextIO

# 符号常量，用于代替序号访问列表数据
ID = 0
NAME = 1
LATITUDE = 2
LONGITUDE = 3
CAPACITY = 4
BIKES_AVAILABLE = 5
DOCKS_AVAILABLE = 6
NO_KIOSK = 'SMART'


# 注，可将函数定义参数中冒号后的类型名删除，箭头及箭头后面的类型删除
# 例如：
# def csv_to_list(csv_file: str) -> List[str]:
# 可修改为：
# def csv_to_list(csv_file):
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


def return_bike(station_id,stations_lst):
    """接收还车站点id和站点数据列表为参数，完成还车功能，返回布尔值"""
    # 补充你的代码
    flag = True

    for line in stations_lst:
        _id = line[ID]

        if _id == station_id:
            line[BIKES_AVAILABLE] += 1
            line[DOCKS_AVAILABLE] -= 1
            
            print(line)
            break


if __name__ == '__main__':
    stations_ls = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(stations_ls)
    return_stat_id = int(input())  # 输入还车站点id
    return_bike(return_stat_id, stations_ls)
