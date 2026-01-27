def factorial(n):
    """接收一个非负整数n为参数，返回n的阶乘，0的阶乘值为1"""
    ######################Begin###############################
    if not n:
        return 1

    return n * factorial(n - 1)
    ######################End###############################

if __name__ == '__main__':
    x = int(input())
    return_data = factorial(x)
    print(return_data)
