def read_file(file,m):
    """读文件中的学校名到列表中，返回排名前m学校集合"""
    ########## Begin ##########
    with open(file, 'r', encoding = 'utf-8') as f:
        lines = f.read().strip().replace('  ', ' ').split('\n')

    school_list = []

    for line in lines:
        line = line.split(' ')
        school = line[1]
        school_list.append(school)

    school_list = school_list[:m]

    return set(school_list)
    ########## End ##########


def either_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在这两个排行榜中均名列前m的学校名，按照学校名称排序，
    返回排序后的列表
    """
    ########## Begin ##########
    res = alumni & soft
    
    ls = [school for school in res]
    ls.sort()

    return ls
    ########## End ##########


def all_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在两个榜单中名列前m的所有学校名，按照学校名称排序，
    返回排序后的列表
    """
    ########## Begin ##########
    res = alumni | soft

    ls = [school for school in res]
    ls.sort()

    return ls
    ########## End ##########


def only_alumni(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在alumni榜单中名列前m但soft榜单中未进前m的学校名，
    按照学校名称排序，返回排序后的列表
    """
    ########## Begin ##########
    res = alumni - soft

    ls = [school for school in res]
    ls.sort()

    return ls
    ########## End ##########


def only_once(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在alumni和soft榜单中名列前m，但不同时出现在两个榜单的学校名，
    按照学校名称排序，返回排序后的列表
    """
    ########## Begin ##########
    res = alumni ^ soft

    ls = [school for school in res]
    ls.sort()

    return ls
    ########## End ##########


def select_first(n):
    """
    接收一个字符
    判断这个字符是否属于 1234 中的一个字符，如果不是则输出 Wrong Option
    如果是，则调用 select_again() 函数
    """
    ########## Begin ##########  
    if n in '1234':
        select_again(n)
    else:
        print('Wrong Option')
    ########## End ##########

def select_again(n):
    """
    接收一个字符
    按左侧 任务要求->问题描述->输入输出 的规则判断 n ，并吊用上面定义的相应的函数
    按左侧 任务要求->测试说明->预期输出 的样例进行输出
    """  
    m=int(input())  
    alumni_set = read_file('step1/alumni.txt',m)  
    soft_set = read_file('step1/soft.txt',m)

    ########## Begin ##########  
    if n == '1':
        print(f'两榜单中均名列前{m}的学校：')
        print(either_in_top(alumni_set, soft_set))
    elif n == '2':
        print(f'两榜单名列前{m}的所有学校：')
        print(all_in_top(alumni_set, soft_set))
    elif n == '3':
        print(f'alumni中名列前{m}，soft中未进前{m}的学校：')
        print(only_alumni(alumni_set, soft_set))
    elif n == '4':
        print(f'不同时出现在两个榜单前{m}的学校：')
        print(only_once(alumni_set, soft_set))
    ########## End ##########

    
    
if __name__ == '__main__':  
    n=input()  
    select_first(n)
