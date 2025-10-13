import pandas as pd
import math

# 定义符号常量，用于索引，使之具有清晰的语义
NUMBER = 0
COUNTRY = 1
DESCRIPTION = 2
POINTS = 3
PRICE = 4

def csv_to_ls(file):
    """接收文件名为参数，用pandas读取文件中的数据，数据部分转为二维列表类型，返回二维列表。"""
    wine_list = pd.read_csv(file).values.tolist()
    return wine_list

def country_ls(wine_list):
    """接收列表格式的葡萄酒数据为参数，略过标题行，返回不重复的国家名列表，按字母表升序排序，
    若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    country_list = []
    for x in wine_list:
        if x[COUNTRY] not in country_list:
            country_list.append(x[COUNTRY])
    country_list.sort()
    # print(country_list)
    return country_list

def avg_point_sort(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表，按评分由高到低降序排列。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 country：国家名，列表类型
    """
    # 此处补充你的代码
    country_dir = {}
    point_dir = {}
    res = []

    for x in wine_list:
        country_temp = x[COUNTRY]
        point = x[POINTS]

        if country_temp not in country_dir:
            country_dir[country_temp] = 1
            point_dir[country_temp] = point
        else:
            country_dir[country_temp] += 1
            point_dir[country_temp] += point

    for x in country:
        count = country_dir[x]
        sum = point_dir[x]

        res.append([x, round(sum / count, 2)])

    return sorted(res, key = lambda x: -x[1])

def top_10_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回评分最高的十款葡萄酒的编号、出产国、评分和价格，按评
    分降序输出。
    需要注意的是评分可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    # 此处补充你的代码
    res = []

    for x in wine_list:
        point = x[POINTS]

        if not math.isnan(point):
            res.append([x[NUMBER], x[COUNTRY], point, x[PRICE]])

    res.sort(key = lambda x: -x[2])

    return res[:10]

def judge(txt):
    """接收一个字符串为参数，根据参数值调用不同函数完成任务"""
    filename = 'data/winemag-data.csv'
    wine = csv_to_ls(filename)
    country = country_ls(wine)
    if txt == '平均分排序':
        print(avg_point_sort(wine, country))  # 每个国家的葡萄酒的平均得分降序输出
    elif txt == '评分最高':
        print(top_10_point(wine))  # 评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出
    else:
        print('输入错误')

if __name__ == '__main__':
    text = input()
    judge(text)
