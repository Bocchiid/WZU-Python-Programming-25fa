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
    """判断当前数据是否是数值，返回布尔型。  """
    # 请补充你的代码
    try:
        float(value)
        return True
    except:
        return False

def clean_data(stations_lst):
    """将数据中的数值字符串转为整数或浮点数：
    若当前数值字符串中的数据是非负整数时，转为int类型；若当前数值字符串中的数据不是非负整数时转为float类型  """
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


def query_available_bikes(stations_lst):
    """查询带各站点可用单车数量信息，返回各站点可用单车总数量 """
    # 请补充你的代码
    sum = 0
    flag = True

    for line in stations_lst:
        if flag:
            flag = False
            continue

        sum += line[BIKES_AVAILABLE]
    
    return sum


def get_stations_id(stations_name, stations_lst):
    """接收一个站点名称和经过数据清洗的站点信息列表，模糊查询站点id，返回包含输入的站名名的全部站点名和对应的id
    仅返回'stat_id', 'name','num_bikes_available','num_docks_available'四列数据，
    标题行设为'stat_id', 'name','bikes','docks'
    """
    # 请补充你的代码
    stations_id = [['stat_id', 'name','bikes','docks']]  # 此为标题行，取消注释后生效

    for line in stations_lst:
        name = line[NAME]

        if stations_name in name:
            stat_id = line[ID]
            bikes = line[BIKES_AVAILABLE]
            docks = line[DOCKS_AVAILABLE]

            ls = [stat_id, name, bikes, docks]

            stations_id.append(ls)

    return stations_id


def menu(stations_id):
    """接收站点查询结果列表，先逐行输出，再返回可选站点id列表
    输出格式：f'{raw[0]:<9}{raw[1]:<35}{raw[2]:<6}{raw[3]:<5}'
        """
    # 请补充你的代码
    id_lst = ['stat_id']
    flag = True

    for raw in stations_id:
        print(f'{raw[0]:<9}{raw[1]:<35}{raw[2]:<6}{raw[3]:<5}')

        if flag:
            flag = False
            continue

        _id = raw[0]
        bikes = raw[2]

        if bikes > 0:
            id_lst.append(_id)

    return id_lst


def rent_bike(station_id,id_ls,  stations_lst):
    """接收借车站点id、站点id列表和站点数据列表为参数，完成借车功能，返回布尔值"""
    # 请补充你的代码
    print(id_ls)

    flag = False

    for _id in id_ls:
        if is_number(_id) is False:
            continue

        if _id == station_id:
            flag = True
            break

    if flag:
        for line in stations_lst:
            _id = line[ID]
            bikes = line[BIKES_AVAILABLE]

            if _id == station_id and bikes > 0:
                line[BIKES_AVAILABLE] -= 1
                line[DOCKS_AVAILABLE] += 1
                
                print(line)
                return True

    return False


if __name__ == '__main__':
    stations_ls = csv_to_list('/data/bigfiles/stations.csv')
    clean_data(stations_ls)
    stat_name = input()
    # print(query_available_bikes(stations_ls))
    stat_id = get_stations_id(stat_name, stations_ls)
    id_lst = menu(stat_id)
    rent_stat_id = int(input())  # 输入借车站点id
    rent_bike(rent_stat_id, id_lst, stations_ls) 
