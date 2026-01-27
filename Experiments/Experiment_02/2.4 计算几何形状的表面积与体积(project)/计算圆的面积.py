import math

def circle(radius):
    """接收圆的半径，返回圆形的面积，圆周率用math.pi"""
    ########################Begin##############################
    pi = 3.14159
    area = pi * radius ** 2

    return f'圆形的面积为{area:.2f}'
    ########################End##############################

if __name__ == '__main__':
    radius = float(input())
    geometry = circle(radius)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果

