import numpy as np

# 设置常量，对应各列数据的语义，方便索引
HIGH = 0
LOW = 1
CLOSE = 3
VOLUME = 4

def statistics_of_all(code_list):
    """
    @参数 code_list：股票代码列表，列表类型
    接收股票数据文件名列表，逐个统计各股票数据文件涨跌幅、总成交量、最高价和最低价。
    涨跌幅计算公式为：(最新记录收盘价-最早记录收盘价) / 最早记录收盘价 * 100
    为方便处理，读入数据时，略过日期列。
    """
    statistics_of_stock = []
    for code in code_list:
        data_of_code = np.genfromtxt('datas/' + code, dtype=None,
                                     usecols=[1, 2, 3, 4, 5, 6], delimiter=',',
                                     skip_header=1)
        # 计算当前股票跌幅、总成交量、最高价和最低价
        uplift_or_fall = round((data_of_code[:, CLOSE][-1] - data_of_code[:, CLOSE][0]) / data_of_code[:, CLOSE][0] * 100, 2)
        volumes = round(sum(data_of_code[:, VOLUME]), 2)
        high = round(max(data_of_code[:, HIGH]), 2)
        low = round(min(data_of_code[:, LOW]), 2)
        statistics_of_stock.append([code[:6], uplift_or_fall, volumes, high, low])
    return statistics_of_stock  # 每支股票涨跌幅、总成交量、最高价和最低价


def top_10_uplift(statistics_of_stock):
    """
    @参数 statistics_of_stock：每支股票涨跌幅、总成交量、最高价和最低价统计信息，列表类型
    按涨幅降序排序，涨幅相同时按股票代码降序排序，取排名前10的股票，
    返回排名前10的股票代码，返回值为列表类型。
    """
    # 补充你的代码
    statistics_of_stock.sort(key = lambda x: (x[1], x[0]), reverse = True)

    return [statistics_of_stock[i][0] for i in range(10)]


def top_10_fall(statistics_of_stock):
    """
    @参数 statistics_of_stock：每支股票涨跌幅、总成交量、最高价和最低价统计信息，列表类型
    按跌幅升序排序，跌幅相同时，按股票代码升序排序，取排名前10的股票，返回跌幅最大的10支股
    票代码的集合。
    """
    # 补充你的代码
    statistics_of_stock.sort(key = lambda x: (x[1], x[0]))

    return [statistics_of_stock[i][0] for i in range(10)]


def top_10_low(statistics_of_stock):
    """
    @参数 statistics_of_stock：每支股票涨跌幅、总成交量、最高价和最低价统计信息，列表类型
    按最低价升序排序，最低价相同时，按股票代码升序排序，取排名前10的股票，返回最低价最低的
    10支股票代码集合。
    """
    # 补充你的代码
    statistics_of_stock.sort(key = lambda x: (x[4], x[0]))

    return [statistics_of_stock[i][0] for i in range(10)]


def low_and_fall(top_fall, top_low):
    """
    @参数 top_low，最低价在前10名的股票代码，字符串
    @参数 top_fall，跌幅在前10名的股票代码，字符串
    返回一个列表，其元素依序为以下4个
    跌幅和最低价均在前10名的股票代码,按股票代码升序，列表
    跌幅或最低价在前10名的股票代码,按股票代码升序，列表
    跌幅前10名，但最低价未进前10名的股票代码,按股票代码升序，列表
    跌幅和最低价不同时在前10名的股票,按股票代码升序，列表
    """
    # 补充你的代码
    f_set = set(top_fall)
    l_set = set(top_low)

    f_and_l_0 = f_set & l_set
    f_and_l_1 = f_set | l_set
    f_and_l_2 = f_set - l_set
    f_and_l_3 = f_set ^ l_set

    ls_0 = [x for x in f_and_l_0]
    ls_0.sort()
    ls_1 = [x for x in f_and_l_1]
    ls_1.sort()
    ls_2 = [x for x in f_and_l_2]
    ls_2.sort()
    ls_3 = [x for x in f_and_l_3]
    ls_3.sort()

    return [ls_0, ls_1, ls_2, ls_3]


def operation():
    """接收一个字符串为参数，根据参数值调用不同函数完成任务"""
    statistics_of_list = statistics_of_all(stock_lst)  # 对获取的股票数据进行统计
    fall_set = top_10_fall(statistics_of_list)  # 跌幅前10名集合
    low_set = top_10_low(statistics_of_list)  # 最低价前10名集合
    f_and_l = low_and_fall(fall_set, low_set)
    opt = input()
    if opt == '跌幅与最低价':
        # 补充你的代码
        print('跌幅和最低价均在前10名的股票:')
        print(f_and_l[0])
        print('跌幅或最低价在前10名的股票:')
        print(f_and_l[1])
        print('跌幅前10名，但最低价未进前10名的股票:')
        print(f_and_l[2])
        print('跌幅和最低价不同时在前10名的股票:')
        print(f_and_l[3])
    else:
        print('输入错误')


if __name__ == '__main__':
    filename = 'datas/沪市股票top300.csv'              # 股票名称与代码文件
    stock_lst = ['600000.csv', '600004.csv', '600006.csv',
                 '600007.csv', '600008.csv', '600009.csv',
                 '600010.csv', '600011.csv', '600012.csv',
                 '600015.csv', '600016.csv', '600018.csv',
                 '600019.csv', '600020.csv', '600026.csv',
                 '600028.csv', '600029.csv', '600030.csv',
                 '600031.csv', '600033.csv', '600036.csv']
    operation()
