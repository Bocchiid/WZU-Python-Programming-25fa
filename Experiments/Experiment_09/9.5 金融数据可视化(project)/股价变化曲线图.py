import pandas as pd
import mplfinance as mpf
import warnings


def pd_read_file(filename):
    """读取文件时，将date列读取为index，此时索引类型为obj，将索引类型更改为DatetimeIndex"""
    df = pd.read_csv(filename, index_col = 'Date')
    df.index = pd.DatetimeIndex(df.index)

    return df


def plot_mpf_price(df_data):
    """ 读取数据绘制 2020 年 9 月至 10 月的股价变化曲线。类型为 line ，线条颜色为绿色 """
    mpf.plot(
        data = df_data,
        type = 'line',
        linecolor = 'green',
        ylabel = 'Price',
        savefig = 'result/result.jpg'
    )


if __name__ == '__main__':
    file = '600132202009.csv'          # 文件名
    df_stock = pd_read_file(file)      # 读文件返回dataframe类型数据
    warnings.filterwarnings('ignore')  # 忽略警告
    plot_mpf_price(df_stock)           # 调用函数绘图
