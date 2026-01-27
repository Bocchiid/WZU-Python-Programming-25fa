#  补充你的代码

a = float(input())
b = float(input())
c = float(input())

flag = False

if a + b > c and a + c > b and b + c > a:
    if a ** 2 + b ** 2 == c ** 2:
        flag = True

print(flag)
