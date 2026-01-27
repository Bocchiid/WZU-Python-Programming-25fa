def my_pow(x, y):
    if not y:
        return 1

    return x * my_pow(x, y - 1)

x = int(input())
y = int(input())

print(my_pow(x, y))
