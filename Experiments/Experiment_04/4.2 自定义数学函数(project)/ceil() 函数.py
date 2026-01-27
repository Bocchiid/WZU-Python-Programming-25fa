def ceil(x):
    """接受一个浮点数或整数，返回大于或等于该数的最小整数"""
    ######################Begin###############################
    if x == int(x):
        return int(x)

    if x < 0:
        return int(x)
    
    return int(x) + 1
    ######################End###############################

if __name__ == '__main__':
    x = eval(input())
    return_data = ceil(x)
    print(return_data)
