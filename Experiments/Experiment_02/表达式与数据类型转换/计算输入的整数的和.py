# 补充你的代码

s = input()
list = s.split()

sum = 0

for item in list:
    if (item.isdigit()):
        sum += int(item)

print(sum)
