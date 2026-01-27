def lcm(a, b):
    """接收两个正整数为参数，以整数类型返回两个数的最小公倍数"""
    ######################Begin###############################
    temp_a, temp_b = a, b

    while b:
        r = a % b
        a = b
        b = r

    return temp_a * temp_b // a
    ######################End###############################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    return_data = lcm(a,b)
    print(return_data)
