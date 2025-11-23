import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文宋体
plt.rcParams['axes.unicode_minus'] = False


def read_txt(filename):
    """读数据文件，返回字符串"""
    with open(filename, 'r', encoding = 'utf-8') as f:
        return f.read()


def plot_line(tiobe):
    """绘制编程语言热度曲线，python曲线宽度设为4，其他语言曲线宽度设为2。
    程序语言名做为线标签，无返回值"""
    plt.figure(figsize=(12, 8))  # 宽度和高度，单位为百像素
    plt.grid(which='major', axis='y', color='b', linestyle='-.', linewidth=0.7)

    x_pos = []
    x_label = []

    it = next(iter(tiobe[0].values()))
    found = False

    for d in it:
        year = f'{d[0][0]}'
        month = f'{d[0][1]:02}'
        day = f'{d[0][2]:02}'
        date = year + '-' + month + '-' + day

        if int(year) % 2 == 0 and month == '05':
            x_pos.append(date)
            x_label.append(year)
        elif year == '2010' and month == '06' and not found:
            x_pos.append(date)
            x_label.append(year)
            found = True

    for dic in tiobe:
        for key, value in dic.items():
            width = 4 if key == 'Python' else 2

            x = [f'{d[0][0]}-{d[0][1]:02}-{d[0][2]:02}' for d in value]
            y = [d[1] for d in value]

            plt.plot(x, y, label = key, linewidth = width)
    
    plt.xticks(x_pos, x_label)
    plt.legend(bbox_to_anchor=(0., -0.12, 1., -.12), loc=8, ncol=5, mode="expand", borderaxespad=0.)


def plot_label():
    """横坐标刻度为偶数年份，图名'The TIOBE Programming Community index'，y标签'热度'，图注位置为'lower left'"""
    plt.title('The TIOBE Programming Community index')
    plt.ylabel('热度')


if __name__ == '__main__':
    tiobe_index = read_txt('step3/tiobe202211.txt')
    tiobe_index = eval(tiobe_index.replace('name : ', '').replace(',data ', '').replace('Date.UTC', ''))  # 字符串替换，再转python数据类型
    plot_line(tiobe_index)
    plot_label()
    plt.savefig('result/result.jpg')
    plt.show()
