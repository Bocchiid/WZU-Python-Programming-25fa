import matplotlib.pyplot as plt


def read_file(file):
    """参数文件名读文件，根据制表符'\t'将每行数据切分为列表再加入到列表中将数据映射为浮点数类型。  
    返回值为二维列表。 """
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = [list(map(float, line.strip().split('\t'))) for line in f]

    return lines


def plot_band_a(band_data):
    """参数数据是二维列表，x值从0-1的变化数据为一组，分组读取数据并绘制全部曲线"""
    x, y = [], []

    for _x, _y in band_data:
        x.append(_x)
        y.append(_y)

        if _x == 1:
            plt.plot(x, y)
            x, y = [], []


if __name__ == '__main__':
    filename = 'band.txt'
    data = read_file(filename)        # 读文件到二维列表
    plot_band_a(data)                 # 调用函数绘制曲线
    plt.savefig("result/result.jpg")  # 保存成图片
    plt.show() 
