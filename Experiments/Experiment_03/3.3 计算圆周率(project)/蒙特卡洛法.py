import random

def monte_carlo_pi(num):
    """接收正整数为参数，表示随机点的数量，利用蒙特卡洛方法计算圆周率
    返回值为表示圆周率的浮点数"""
    # 补充你的代码
    cnt = 0

    for i in range(num):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        dist_squared = x ** 2 + y ** 2

        if (dist_squared < 1):
            cnt += 1

    return cnt / num * 4

if __name__ == '__main__':
    sd = int(input())             #读入随机数种子
    random.seed(sd)               #设置随机数种子
    times = int(input())          # 输入正整数，表示产生点数量
    print(monte_carlo_pi(times))  # 输出圆周率值，浮点数
