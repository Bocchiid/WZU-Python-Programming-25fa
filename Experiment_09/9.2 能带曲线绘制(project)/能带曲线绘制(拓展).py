import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

def read_file(file):
    """参数文件名读文件，根据制表符'\t'将每行数据切分为列表再加入到列表中将数据映射为浮点数类型。
    返回值为二维列表。 """
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = [list(map(float, line.strip().split('\t'))) for line in f]

    return lines    


def plot_band(data_list, m, n):
    """参数数据是二维列表，x值从0-1的变化数据为一组，m, n：用户输入的y轴取值范围，分组读取数据并绘制全部曲线"""
    x, y = [], []

    for _x, _y in data_list:
        x.append(_x)
        y.append(_y)

        if _x == 1:
            if all(m <= item <= n for item in y):
                plt.plot(x, y)
            x, y = [], []


def bottom_top_band(data_list):
    """参数是浮点数的二维列表,定位导价底和价带顶的坐标。导带底为纵坐标大于0的部曲线最低点，
    价带顶为纵坐标小于0 的曲线最高点，一般导带底与价带顶相对，即横坐标相同。以元组形式返回导带底坐标和价带顶坐标 """
    up = [(d[0], d[1]) for d in data_list if d[1] > 0]
    up.sort(key = lambda x: x[1])
    bottom = up[0]

    down = [(d[0], d[1]) for d in data_list if d[1] < 0]
    down.sort(key = lambda x: -x[1])

    for item in down:
        if item[0] == bottom[0]:
            return tuple(bottom), tuple(item)

def gap_of_band(bottom, top):
    """bottom纵坐标大于0的部曲线最低点坐标；top纵坐标小于0 的曲线最高点坐标
    接收导带底和价带顶的数值，带隙为导带底和价带顶纵坐标之差，返回带隙值。 """
    return bottom[1] - top[1]


def mark_peak(bottom_top):
    """绘制注释，在y值大于0的部分找到曲线最低点，标注'bottom of conduction band'
    在y值小于0的部分找到曲线最高点，标注'top of valence band'。 绘制导带底到价带顶连线，灰色破折线 """
    plt.plot([bottom_top[0][0], bottom_top[1][0]], [bottom_top[0][1], bottom_top[1][1]], linestyle='--', color='gray') 
    plt.annotate(r'bottom of conduction band', xy=bottom_top[0], xytext=(-200, -20),
                 textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.annotate(r'top of valence band', xy=bottom_top[1], xytext=(0, 15),
                 textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))


def plot_label():
    """绘制x轴和坐标标签、图名"""
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
    bottom_to_top = bottom_top_band(data)
    mark_peak(bottom_to_top)
    plot_label()
    bottom_top_band(data)
    plt.savefig("result/result.jpg")  # 保存成图片
    plt.show()
