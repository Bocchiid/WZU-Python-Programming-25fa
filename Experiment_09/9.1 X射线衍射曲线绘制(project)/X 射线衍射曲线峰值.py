import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False


def read_file(file):
    """ 读文件file， 返回值为二维列表，其中数据是字符串类型。 """
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = [line.strip().split() for line in f]
        lines = lines[1:]

    return [[eval(line[0]), eval(line[1])] for line in lines]


def top_five_peak(data_list):
    """参数为读文件获得的数据列表，返回纵坐标值最大的5个峰的坐标的列表，降序排序。"""
    ls = sorted(data_list, key = lambda x: -x[1])

    return ls[:5]


def plot_xrd(data_list):
    """接收二维列表为参数，绘制曲线"""
    x = [d[0] for d in data_list]
    y = [d[1] for d in data_list]

    plt.xlim(5, 25)
    plt.plot(x, y, 'r')


def mark_peak(peak_ls):
    """参数为峰值数据列表，在指定的坐标点加注释。注释标记点相对横坐标偏移+30，纵坐标等高，
    注释文本为峰高，即y 值，注释文本字号为12，箭头类型"->"。
    """
    for x, y in peak_ls:
        plt.annotate(f'{y}', xy=(float(x), float(y)), xytext=(+30, 0),
                     textcoords='offset points', fontsize=12,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


def add_label():
    """增加坐标轴标识与图名"""
    plt.title('X射线衍射图谱')
    plt.xlabel('2d')
    plt.ylabel('Intensity')
    plt.axhline(linestyle = '--', color = 'b')


if __name__ == '__main__':
    data = read_file('XRD_AFO.txt')
    peak_lst = top_five_peak(data)
    plot_xrd(data)
    mark_peak(peak_lst)
    add_label()
    plt.savefig('result/result.jpg')
    plt.show()
