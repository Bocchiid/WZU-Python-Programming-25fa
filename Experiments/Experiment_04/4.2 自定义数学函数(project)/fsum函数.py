def fsum(iterable):
    """接收一个元素为数值的序列为参数，以浮点数类型返回各元素之和"""
    ######################Begin###############################
    sum = 0.0

    for item in iterable:
        sum += item

    return sum
    ######################End###############################

if __name__ == '__main__':
    x = list(map(eval, input().split()))
    return_data = fsum(x)
    print(return_data)
