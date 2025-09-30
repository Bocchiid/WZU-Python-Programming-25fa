def gcd(a, b):
    """接收两个正整数为参数，返回两个数的最大公约数"""
    #######################Begin############################
    while b:
        r = a % b
        a = b
        b = r

    return a
    #######################End############################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    return_data = gcd(a,b)
    print(return_data)
