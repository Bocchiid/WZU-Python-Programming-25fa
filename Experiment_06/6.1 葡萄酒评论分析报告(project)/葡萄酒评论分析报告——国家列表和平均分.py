import pandas as pd

# 定义符号常量，用于索引，使之具有清晰的语义
COUNTRY = 1
POINTS = 3

def csv_to_ls(file):
    """接收文件名为参数，用pandas读取文件中的数据，数据部分转为二维列表类型，返回二维列表。"""
    wine_list = pd.read_csv(file).values.tolist()
    return wine_list

def country_ls(wine_list):
    """接收列表格式的葡萄酒数据为参数，略过标题行，返回不重复的国家名列表，按字母表升序排序，
    若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    # 此处补充你的代码
    res = []

    for each in wine_list:
        country = each[COUNTRY]

        if country not in res:
            res.append(country)

    return sorted(res)

def avg_point(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 country：国家名，列表类型
    """
    # 此处补充你的代码
    point_dir = {}
    country_dir = {}
    res = []

    for each in wine_list:
        country_temp = each[COUNTRY]
        point = each[POINTS]

        if country_temp not in country_dir:
            country_dir[country_temp] = 1
            point_dir[country_temp] = point
        else:
            country_dir[country_temp] += 1
            point_dir[country_temp] += point

    for each in country:
        count = country_dir[each]
        sum = point_dir[each]

        res.append([each, round(sum / count, 2)])

    return res

def judge(txt):
    """接收一个字符串为参数，根据参数值调用不同函数完成任务"""
    filename = 'data/winemag-data.csv'
    wine = csv_to_ls(filename)
    country = country_ls(wine)
    if txt == '国家名列表':
        print(country)
    elif txt == '平均分':
        print(avg_point(wine, country))  # 每个国家的葡萄酒的平均得分
    else:
        print('输入错误')

if __name__ == '__main__':
    text = input()
    judge(text)
