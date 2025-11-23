import pandas as pd
import mplfinance as mpf
import warnings
import matplotlib.pyplot as plt


def pd_read_file(filename):
    """读取文件时，将date列读取为index，此时索引类型为obj，将索引类型更改为DatetimeIndex"""
    df = pd.read_csv(filename, index_col = 'Date')
    df.index = pd.DatetimeIndex(df.index)

    return df


def plot_mpf_charles(df):
    """ df为pandas.DataFrame类型，必须包含’Open’, ‘High’, ‘Low’ 和 ‘Close’ 数据
    绘制类型为`candle`，并带 2 日、5 日和 10 日均线，样式为`charles`，显示成交量"""
    mpf.plot(
        data = df,
        type = 'candle',
        ylabel = 'Price',
        mav = (2, 5, 10),
        volume = True,
        style = 'charles',
    )


if __name__ == '__main__':
    file = '600132202009.csv'  # 文件名
    warnings.filterwarnings('ignore')  # 忽略警告
    df_stock = pd_read_file(file)
    plot_mpf_charles(df_stock)
    plt.savefig('result/result.jpg')
    plt.show()
