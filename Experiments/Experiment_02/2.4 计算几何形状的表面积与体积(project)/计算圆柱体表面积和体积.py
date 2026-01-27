import math

def cylinder(radius, height):
    """接收圆柱体的底面半径和高，返回圆柱体的表面积和体积，圆周率用math.pi"""
    ########################Begin##############################
    pi = 3.14159
    area = 2 * pi * radius * (radius + height)
    volumn = pi * radius ** 2 * height

    return f'圆柱体的表面积为{area:.2f}, 体积为{volumn:.2f}'
    ########################End##############################

if __name__ == '__main__':
    radius, height = map(float, input().split())
    geometry = cylinder(radius, height)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果
