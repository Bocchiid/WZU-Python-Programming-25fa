import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False


def read_file(file):
    """ 读文件file， 返回值为二维列表，其中数据是字符串类型。 """
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = [line.strip().split() for line in f]
        lines = lines[1:]

    return [[eval(line[0]), eval(line[1])] for line in lines]


def plot_xrd(data_list):
    """接收二维列表为参数，绘制曲线，红色实线"""
    x = [d[0] for d in data_list]
    y = [d[1] for d in data_list]

    plt.plot(x, y, 'r')


def add_label():
    """增加坐标轴标识与图名"""
    plt.title('X射线衍射图谱')
    plt.xlabel('2d')
    plt.ylabel('Intensity')
    plt.axhline(linestyle = '--', color = 'b')
    plt.axvline(linestyle = '--', color = 'r')


if __name__ == '__main__':
    data = read_file('XRD_AFO.txt' )
    plot_xrd(data)
    add_label()
    plt.savefig('result/result.jpg')
    plt.show()
