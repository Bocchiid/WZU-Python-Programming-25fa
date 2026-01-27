import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，只保留文件中的英文字母和西文符号，过滤掉中
    文，所有字符转为小写，将其中所有标点、符号替换为空格，返回字符串。"""
    with open(file, 'r', encoding = 'utf-8') as f:
        text = f.read().strip()

    text = ''.join(c for c in text if ord(c) < 256)
    text = text.lower()

    for c in string.punctuation:
        text = text.replace(c, ' ')

    return text


def draw_cloud_en_txt(text):
    """参数text读文件获取的文本，绘制词云，显示高频单词数量为80个，
    图片的宽度600，高度400，背景白色、字体最大值150、图片边缘为5，
    放大画布1.5倍，不随机(random_state=False)，不显示坐标轴，
    词云保存为图片，路径和名为：'result/result.png' """
    wc = WordCloud(
        width = 600,
        height = 400,
        background_color = 'white',
        max_font_size = 150,
        margin = 5,
        scale = 1.5,
        random_state = False,
        max_words = 80,
    ).generate_from_text(text)

    plt.axis('off')

    wc.to_file('result/result.png')


if __name__ == '__main__':
    filename = '/data/bigfiles/Who_Moved_My_Cheese.txt'  # 英文文件名
    content = read_file(filename)         # 调用函数返回字典类型的数据
    draw_cloud_en_txt(content)
