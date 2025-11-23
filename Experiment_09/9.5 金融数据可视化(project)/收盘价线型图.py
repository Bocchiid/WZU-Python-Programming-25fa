import matplotlib.pyplot as plt

# 设置常量，对应各列数据的语义，可用具有语义的常量代替数字做索引和切片
Date = 0    # 日期
HIGH = 1    # 最高价
LOW = 2     # 最低价
OPEN = 3    # 开盘价
CLOSE = 4   # 收盘价
VOLUME = 5  # 日成交量
ADJCLOSE = 6


def read_file(filename):
    """ 接收文件名为参数，读取文件中的数据为二维列表，返回列表"""
    # 补充你的代码
    with open(filename, 'r', encoding = 'utf-8') as f:
        lines = [line.strip().split(',') for line in f]

    return lines[1:]


def stock_2020_9(data_list):
    """参数 包含股票的数据的二维列表，返回2020年9月1日至9月31日收盘价数据的列表"""
    # 补充你的代码
    return [[x[Date], eval(x[CLOSE])] for x in data_list if x[Date].split('-')[1] == '09']



def plot_stock(data_list):
    """参数 包含股票的数据的二维列表，绘制2020年9月股价变化线型图
    以日期为横坐标，旋转30度显示，股价点用'*'标记。
    """
    x = [item[0] for item in data_list]
    y = [item[1] for item in data_list]

    plt.plot(x, y, marker = '*')
    plt.xticks(rotation = 30)       


if __name__ == '__main__':
    file = '600132202009.csv'  # 文件名
    stock_in_list = read_file(file)
    stock_of_2020_9 = stock_2020_9(stock_in_list)
    plot_stock(stock_of_2020_9)
    plt.savefig('result/result.jpg')
    plt.show() 
