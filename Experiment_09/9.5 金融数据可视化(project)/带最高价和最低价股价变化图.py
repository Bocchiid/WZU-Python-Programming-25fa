import pandas as pd
import mplfinance as mpf
import warnings
import matplotlib.pyplot as plt


def pd_read_file(filename):
    """读取文件时，将date列读取为index，此时索引类型为obj，将索引类型更改为DatetimeIndex"""
    df = pd.read_csv(filename, index_col = 'Date')
    df.index = pd.DatetimeIndex(df.index)

    return df    


def plot_mpf_add_plot(df):
    """ df为pandas.DataFrame类型，必须包含’Open’, ‘High’, ‘Low’ 和 ‘Close’ 数据
    绘制带最高价和最低价股价变化图，类型为`candle`，同时显示最高价和最低价"""
    add_plot = mpf.make_addplot(df[['High', 'Low']])
    
    mpf.plot(
        data = df,
        type = 'candle',
        ylabel = 'Price',
        addplot = add_plot
    )


if __name__ == '__main__':
    file = '600132202009.csv'  # 文件名
    warnings.filterwarnings('ignore')  # 忽略警告
    df_stock = pd_read_file(file)
    plot_mpf_add_plot(df_stock)
    plt.savefig('result/result.jpg')
    plt.show()
