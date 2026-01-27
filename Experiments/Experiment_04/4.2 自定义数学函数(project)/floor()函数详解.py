def floor(x):
    """接受一个浮点数或整数，返回不大于该数的最大整数"""
    ######################Begin###############################
    if x == int(x):
        return int(x)

    if x < 0:
        return int(x) - 1

    return int(x)
    ######################End###############################
    
if __name__ == '__main__':
    x = eval(input())
    return_data = floor(x)
    print(return_data)
