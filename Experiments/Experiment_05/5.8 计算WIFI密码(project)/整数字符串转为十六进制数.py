def my_pow(x, y):
    if not y:
        return 1

    return x * my_pow(x, y - 1)

x = int(input())
y = int(input())

result = str(my_pow(x, y))
result = result[:16]

hex_result = hex(int(result))

print(hex_result)
