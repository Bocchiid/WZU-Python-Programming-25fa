import pandas as pd
import mplfinance as mpf
import warnings
import matplotlib.pyplot as plt


def pd_read_file(filename):
    """读取文件时，将date列读取为index，此时索引类型为obj，将索引类型更改为DatetimeIndex"""
    df = pd.read_csv(filename, index_col = 'Date')
    df.index = pd.DatetimeIndex(df.index)

    return df


def plot_mpf_mav(df):
    """ df为pandas.DataFrame类型，必须包含’Open’, ‘High’, ‘Low’ 和 ‘Close’ 数据
    增加绘制均线,关键字参数mav = (2, 5, 10)，多条均线使用元组，只绘制一条均线，可以mav = 10；类型为 line"""
    mpf.plot(
        data = df,
        type = 'line',
        ylabel = 'Price',
        mav = (2, 5, 10),
    )


if __name__ == '__main__':
    file = '600132202009.csv'  # 文件名
    warnings.filterwarnings('ignore')  # 忽略警告
    df_stock = pd_read_file(file)
    plot_mpf_mav(df_stock)
    plt.savefig('result/result.jpg')
    plt.show()
