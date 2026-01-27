import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文宋体
plt.rcParams['axes.unicode_minus'] = False


def read_txt(filename):
    """读数据文件，返回字符串"""
    with open(filename, 'r', encoding = 'utf-8') as f:
        return f.read()


def draw_pie(tiobe):
    x_data = [list(line.values())[-1][-1][-1] for line in tiobe]
    x_data = x_data + [100 - round(sum(x_data), 2)]
    x_label = []
    x_explode = []
    
    for dic in tiobe:
        for key, value in dic.items():
            x_label.append(key)

            if key == 'Python':
                x_explode.append(0.1)
            else:
                x_explode.append(0)

    x_label.append('other')
    x_explode.append(0)

    plt.pie(
        x = x_data,
        labels = x_label,
        explode = x_explode,
        pctdistance = 0.8,
        startangle = 90,
        autopct = '%2.1f%%',
        shadow = True,
        labeldistance = 1.1
    )
    plt.legend(
        loc = 'lower right',
        bbox_to_anchor = (1.3, 0)
    )


if __name__ == '__main__':
    tiobe_index = read_txt('step2/tiobe202211.txt')
    tiobe_index = eval(tiobe_index.replace('name : ', '').replace(',data ', '').replace('Date.UTC', ''))
    draw_pie(tiobe_index)
    plt.savefig('result/result.jpg')
    plt.show()
