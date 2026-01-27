import math

def sphere(radius):
    """接收球的半径，返回球的表面积和体积，圆周率用math.pi"""
    ########################Begin##############################
    pi = 3.14159
    area = 4 * pi * radius ** 2
    volumn = 4 / 3 * pi * radius ** 3

    return f'球的表面积为{area:.2f}, 体积为{volumn:.2f}'
    ########################End##############################

if __name__ == '__main__':
    radius = float(input())
    geometry = sphere(radius)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果 
