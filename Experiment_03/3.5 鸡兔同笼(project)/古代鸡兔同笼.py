# 补充你的代码

heads = 35
feet = 94

for i in range(heads + 1):
    j = heads - i

    if i * 2 + j * 4 == feet:
        print(f'买{i}只鸡，买{j}只兔')
        break
