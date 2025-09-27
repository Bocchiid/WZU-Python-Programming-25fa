import math

def cone(radius, height):
    """接收圆锥的底面半径和高，返回圆锥的表面积和体积，圆周率用math.pi"""
    ########################Begin##############################
    pi = 3.14159
    area = pi * radius * (radius + math.sqrt(radius * radius + height * height))
    volumn = 1 / 3 * pi * radius ** 2 * height

    return f'圆锥的表面积为{area:.2f}, 体积为{volumn:.2f}'
    ########################End##############################

if __name__ == '__main__':
    radius, height = map(float, input().split())
    geometry = cone(radius, height)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果
