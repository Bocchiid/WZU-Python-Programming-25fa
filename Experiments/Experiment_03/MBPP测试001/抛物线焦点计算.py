# 请补充你的代码

a, b, c = map(int, input().split())

x = (-b) / (2 * a)
y = (4 * a * c - b ** 2 + 1) / (4 * a)

print(f'({x:.3f}, {y:.3f})')
