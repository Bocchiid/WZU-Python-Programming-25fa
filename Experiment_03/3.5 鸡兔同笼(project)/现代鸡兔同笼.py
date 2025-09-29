# 补充你的代码

heads, feet = map(int, input().split())

flag = False

for i in range(heads + 1):
    j = heads - i

    if i * 2 + j * 4 == feet:
        print(f'有{i}只鸡，{j}只兔')
        flag = True
        break

if not flag:
    print('Data Error!')
