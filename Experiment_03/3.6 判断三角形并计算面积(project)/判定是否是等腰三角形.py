#  补充你的代码

a = float(input())
b = float(input())
c = float(input())

flag = False

if a + b > c and a + c > b and b + c > a:
    if a == b or a == c or b == c:
        flag = True

print(flag)
