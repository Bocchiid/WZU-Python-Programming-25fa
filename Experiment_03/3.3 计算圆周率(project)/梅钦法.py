'''
利用梅钦公式计算圆周率的大小
'''
import math


def machin_of_pi():
    """用梅钦级数计算圆周率，返回圆周率值"""
    # 补充你的代码
    temp = 4 * math.atan(1 / 5) - math.atan(1 / 239)

    pi = temp * 4

    return pi
    
if __name__ == '__main__':
    cal_pi = machin_of_pi()  # 调用判断类型的函数
    print(cal_pi)            # 输出函数运行结果
