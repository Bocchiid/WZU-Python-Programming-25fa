'''
输入一个正整数n，使用拉马努金法公式计算思加n次时的圆周率值。
'''
import math


def ramanujan_of_pi(n):
    """接收一个正整数n为参数，用拉马努金公式的前n项计算圆周率并返回。"""
    # 补充你的代码
    s = 0

    for k in range(n):
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = math.factorial(k) ** 4 * 396 ** (4 * k)
        s += numerator / denominator

    pi = 1 / ((2 * 2 ** 0.5 / 9801) * s)

    return pi

if __name__ == '__main__':
    n = int(input())                
    cal_pi = ramanujan_of_pi(n)  
    print(cal_pi)                    # 输出函数运行结果
