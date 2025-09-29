# 补充你的代码

heads, feet = map(int, input().split())

flag = False

i, j = 0, 0
k, l = 0, 0

for i in range(heads + 1):
    for j in range(heads + 1 - i):
        for k in range(heads + 1 - i - j):
            for l in range(heads + 1 - i - j - k):
                if j * 3 != i or k * 2 != l:
                    continue

                if (i + k) * 2 + (j + l) * 4 == feet and i + j + k + l == heads:
                    flag = True
                    print(f'A笼中有鸡{i}只，兔{j}只')
                    print(f'B笼中有鸡{k}只，兔{l}只')
                    print(f'两笼共有鸡{i + k}只，兔{j + l}只')
                    break

if not flag:
    print('无合适的组合方案')
