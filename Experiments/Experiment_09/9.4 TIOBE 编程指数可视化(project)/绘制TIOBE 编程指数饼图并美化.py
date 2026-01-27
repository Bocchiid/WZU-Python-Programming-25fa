import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


plt.rcParams['font.sans-serif'] = ['SimSun']  # 中文宋体
plt.rcParams['axes.unicode_minus'] = False


def read_txt(filename):
    """读数据文件，返回字符串"""
    with open(filename, 'r', encoding = 'utf-8') as f:
        return f.read()


def draw_pie(tiobe):
    """绘制饼图，大小1200*800，图例在图上方每行3个，彩虹颜色"""
    plt.figure(figsize=(12, 8))  # 图像大小1200*800像素

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

    rank = [list(line.values())[-1][-1][-1] for line in tiobe]
    rank = rank + [100 - round(sum(rank), 2)]
    colors = cm.rainbow(np.arange(len(rank)) / len(rank)) # colormaps: Paired, autumn, rainbow, gray,spring,Darks

    plt.pie(
        x = rank,
        labels = x_label,
        explode = x_explode,
        colors = colors,
        pctdistance = 0.8,
        startangle = 90,
        autopct = '%2.1f%%',
        shadow = True,
        labeldistance = 1.1
    )
    plt.legend(bbox_to_anchor=(0., 0.96, 1., 0.1), loc=3, ncol=3, mode="expand", borderaxespad=0.) 


if __name__ == '__main__':
    tiobe_index = read_txt('step4/tiobe202211.txt')
    tiobe_index = eval(tiobe_index.replace('name : ', '').replace(',data ', '').replace('Date.UTC', ''))
    draw_pie(tiobe_index)
    plt.savefig('result/result.jpg')
    plt.show()
