import matplotlib.pyplot as plt


def read_file(file):
    """ 读文件file， 返回值为二维列表，其中数据是字符串类型。 """
    # 补充你的代码
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = [line.strip().split() for line in f]
        lines = lines[1:]

    return [[eval(line[0]), eval(line[1])] for line in lines]


def plot_xrd(data_list):
    """接收二维列表为参数，绘制曲线"""
    x_data = [line[0] for line in data_list]
    y_data = [line[1] for line in data_list]  

    plt.plot(x_data, y_data)


if __name__ == '__main__':
    data = read_file('XRD_AFO.txt')
    plot_xrd(data)
    plt.savefig('result/result.jpg')
    plt.show()
