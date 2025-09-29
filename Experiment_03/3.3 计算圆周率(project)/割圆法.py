'''
编程实现割圆法计算圆周率，并输出分割不同次数时边数、圆周率值以及计算所得圆周率值与math库中的圆周率值的偏差。
'''

import math

def cutting_circle(n):      # n为分割次数
    """接收表示分割次数的整数n为参数，计算分割n次时正多边形的边数和圆周率值，返回边数和圆周率值"""
    side_length = 1  # 初始边长
    edges = 6  # 初始边数
    # 补充你的代码
    for i in range(n):
        ab = od = oa = side_length
        ac = bc = ab / 2
        oc = (1 - bc ** 2) ** 0.5
        cd = 1 - oc
        ad = (ac ** 2 + cd ** 2) ** 0.5
        side_length = ad
        edges *= 2

    pi = edges * side_length / 2

    return edges, pi

if __name__ == '__main__':
    times = int(input())          # 割圆次数
    # 补充你的代码
    edges, pi = cutting_circle(times) # 圆周率
    print(f'分割{times}次，边数为{edges}，圆周率为{pi:.6f}')
    print(f'math库中的圆周率常量值为{math.pi:.6f}')
