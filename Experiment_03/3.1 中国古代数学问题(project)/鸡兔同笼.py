"""
在同一行内输入用空格分隔的两个整数，代表头和脚的数量，计算并输出笼中各有多少只鸡和兔，
如无解则输出“Data Error!”，函数无返回值。
输入：35 94
输出：有23 只鸡，12 只兔
输入：100 5
输出：Data Error!
"""
head,feet = map(int, input().split()) #读入以空格分隔的两个整数，表示头和脚的数量
##############Begin#####################
flag = False

for i in range(0, head + 1):
    j = head - i

    if (i * 2 + j * 4 == feet):
        flag = True
        print(f'有{i}只鸡，{j}只兔')

if (not flag):
    print('Data Error!')
##############End#####################
