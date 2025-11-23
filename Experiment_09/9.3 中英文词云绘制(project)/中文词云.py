import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串"""
    # 补充你的代码
    with open(file, 'r', encoding = 'utf-8') as f:
        return f.read()


def word_frequency_cn(txt):
    """参数 txt读文件获取的文本，jieba.analyse.textrank()可用参数topK设置最多返回多少个按词频降序排列的关键词列表，
    数据格式为列表：[('人民', 1.0), ('中国', 0.9533997295396189), ...]，
    将列表转为字典:{'人民': 1.0, '中国': 0.9533997295396189,...}，返回这个字典"""
    ls = jieba.analyse.textrank(txt, topK=60, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))

    return dict(ls)


def draw_cloud_cn(frequency_dict):
    """参数为词频，字典类型，设定图片的中文字体为('fonts/MSYH.TTC')、背景为白色、
    背景图片'ball.jpg'、字体最大值200、按比例进行放大画布2倍，储存为 result/result.png"""
    # 补充你的代码
    mask = np.array(Image.open('ball.jpg'))

    wc = WordCloud(
        font_path = 'fonts/MSYH.TTC',
        background_color = 'white',
        mask = mask,
        max_font_size = 200,
        scale = 2,
        random_state = False
    ).generate_from_frequencies(frequency_dict)

    plt.axis('off')

    wc.to_file('result/result.png')


if __name__ == '__main__':
    filename = '/data/bigfiles/湿地公约.txt'      # 用于生成词云的中文文件名
    content = read_file(filename)
    frequency = word_frequency_cn(content)  # 利用jieba对文本进行分词，并统计词频
    draw_cloud_cn(frequency)                   # 绘制词云
