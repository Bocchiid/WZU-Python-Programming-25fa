# 补充你的代码

list = input()

list = eval(list)
new_list = []

for item in list:
    if (item.isdigit()):
        new_list.append(int(item))

print(new_list)
print(sum(new_list))
