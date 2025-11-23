import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文字体
plt.rcParams['axes.unicode_minus'] = False


def read_file(file):
    """参数文件名读文件，根据制表符'\t'将每行数据切分为列表再加入到列表中将数据映射为浮点数类型。
    返回值为二维列表。 """
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = [list(map(float, line.strip().split('\t'))) for line in f]

    return lines


def plot_band(band_data, m, n):
    """参数数据是二维列表，x值从0-1的变化数据为一组，m, n：用户输入的y轴取值范围，分组读取数据并绘制全部曲线"""
    x, y = [], []

    for _x, _y in band_data:
        if m <= _y <= n:
            x.append(_x)
            y.append(_y)

            if _x == 1:
                if all(m <= item <= n for item in y):
                    plt.plot(x, y)
                x, y = [], []


def plot_label():
    """绘制坐标标签、图名与x轴"""
    plt.title('能带曲线图谱')
    plt.xlabel('k')
    plt.ylabel('E(ev)')
    plt.axhline(linestyle = '--', color = 'r')


if __name__ == '__main__':
    filename = 'band.txt'
    data = read_file(filename)  # 读文件到二维列表
    min_value, max_value = map(float, input().split())  # 输入数据范围
    if min_value > max_value:
        min_value, max_value = max_value, min_value
    plot_band(data, min_value, max_value)  # 调用函数绘制曲线
    plot_label()
    plt.savefig("result/result.jpg")  # 保存成图片
    plt.show()
