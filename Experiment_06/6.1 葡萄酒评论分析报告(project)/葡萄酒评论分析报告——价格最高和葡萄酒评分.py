import pandas as pd
import math

# 定义符号常量，用于索引，使之具有清晰的语义
NUMBER = 0
COUNTRY = 1
POINTS = 3
PRICE = 4

def csv_to_ls(file):
    """接收文件名为参数，用pandas读取文件中的数据，数据部分转为二维列表类型，返回二维列表。"""
    wine_list = pd.read_csv(file).values.tolist()
    return wine_list
    
def top_20_price(wine_list):
    """接收列表格式的葡萄酒数据参数，返回价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价
    格降序输出。
    @参数 wine_list：葡萄酒数据，列表类型
    需要注意的是价格可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    """
    # 此处补充你的代码
    res = []

    for x in wine_list:
        price = x[PRICE]

        if not math.isnan(price):
            res.append([x[NUMBER], x[COUNTRY], x[POINTS], price])

    res.sort(key = lambda x: -x[3])

    return res[:20]

def amount_of_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回每个评分的葡萄酒数量，忽略没有评分的数据
    例如[...[84, 645], [85, 959],...]表示得分为84的葡萄酒645种，得分85的葡萄酒有959种。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    # 此处补充你的代码
    wine_dir = {}

    for x in wine_list:
        point = x[POINTS]

        if point not in wine_dir:
            wine_dir[point] = 1
        else:
            wine_dir[point] += 1

    res = [[k, v] for k, v in wine_dir.items()]
    res.sort(key = lambda x: x[0])

    return res

def most_of_point(amount_of_points):
    """接收每个评分的葡萄酒数量的列表为参数，返回获得该分数数量最多的评分和数量的列表。
    @参数 amount_of_points：每个评分的葡萄酒数量，列表类型
    """
    # 此处补充你的代码
    res = sorted(amount_of_points ,key = lambda x: -x[1])

    return res[0]

def avg_price_of_most_point(wine_list, most_of_points):
    """接收列表格式的葡萄酒数据和获得最多的评分及数量的列表为参数
    忽略缺失价格的数据，返回这个分数的葡萄酒的平均价格，保留2位小数。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 most_of_points：获得最多的评分及数量，列表类型
    """
    # 此处补充你的代码
    count = 0
    sum_of_price = 0

    for x in wine_list:
        point = x[POINTS]
        price = x[PRICE]

        if point == most_of_points[0] and not math.isnan(price):
            count += 1
            sum_of_price += price

    return round(sum_of_price / count, 2)

def judge(txt):
    """接收一个字符串为参数，根据参数值调用不同函数完成任务"""
    filename = 'data/winemag-data.csv'
    wine = csv_to_ls(filename)
    if txt == '价格最高':
        print(top_20_price(wine))  # 价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出
    elif txt == '葡萄酒评分':
        amount_point = amount_of_point(wine)
        most_point = most_of_point(amount_point)
        print(amount_point)  # 各个评分的葡萄酒数量
        print(most_point)  # 拥有葡萄酒数量最多的评分和数量
        print(avg_price_of_most_point(wine, most_point))  # 拥有葡萄酒数量最多的评分的葡萄酒的平均价格
    else:
        print('输入错误')

if __name__ == '__main__':
    text = input()
    judge(text)
