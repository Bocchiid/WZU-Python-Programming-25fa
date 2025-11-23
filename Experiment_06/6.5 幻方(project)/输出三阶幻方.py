# 补充你的代码


ls = []

for i in range(3):
    line = input().split()

    ls.append(line)

    print(line)

for line in ls:
    print(*line)
