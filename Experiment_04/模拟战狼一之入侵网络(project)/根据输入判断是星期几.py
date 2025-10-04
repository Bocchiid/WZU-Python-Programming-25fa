# 请补充你的代码

def f_1(s_1):
    if s_1 == 'm' or s_1 == 'w' or s_1 == 'f':
        return True

    return False

s_1 = input().lower()

if f_1(s_1):
    if s_1 == 'm':
        print('Monday')
    elif s_1 == 'w':
        print('Wednesday')
    elif s_1 == 'f':
        print('Friday')
else:
    s_2 = input().lower()

    if s_1 == 't':
        if s_2 in 'Tuesday' and s_2 not in 'Thursday':
            print('Tuesday')
        elif s_2 not in 'Tuesday' and s_2 in 'Thursday':
            print('Thursday')
        else:
            print('无法匹配')
    elif s_1 == 's':
        if s_2 in 'Saturday' and s_2 not in 'Sunday':
            print('Saturday')
        elif s_2 not in 'Saturday' and s_2 in 'Sunday':
            print('Sunday')
        else:
            print('无法匹配')
