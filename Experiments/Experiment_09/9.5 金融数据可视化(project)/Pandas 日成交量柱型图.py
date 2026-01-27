import matplotlib.pyplot as plt
import pandas as pd


def plot_volume_pd(filename):
    """参数包含路径的数据文件名，利用Pandas 对金融数据进行可视化,绘制日成交量的柱型图。"""
    opened_file = pd.read_csv(filename)

    df = pd.DataFrame(opened_file['Volume'])
    df.plot(kind = 'bar', legend = False)


if __name__ == '__main__':
    file = '600132202009.csv'  # 文件名
    plot_volume_pd(file)       # 调用函数绘制图形
    plt.savefig('result/result.jpg')
    plt.show()
