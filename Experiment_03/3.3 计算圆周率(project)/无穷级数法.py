'''
使用无穷级数这个公式计算π值，输入一个小数作为阈值，当最后一项的绝对值小于给定阈值时停止计算并输出得到的π值
'''

def leibniz_of_pi(error):
    """接收用户输入的浮点数阈值为参数，返回圆周率值"""
    # 补充你的代码
    i = 1
    sign = 1
    sum = 0

    while True:
        temp = 1 / i
        
        if (temp < error):
            break
            
        sum += temp * sign
        i += 2
        sign = -sign
        
    return sum * 4

if __name__ == '__main__':
    threshold = float(input())
    print("{:.8f}".format( leibniz_of_pi(threshold)  ) ) #保留小数点后八位
