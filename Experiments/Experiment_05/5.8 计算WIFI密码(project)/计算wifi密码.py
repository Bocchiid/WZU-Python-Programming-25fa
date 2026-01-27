def my_pow(x, y):
    if not y:
        return 1

    return x * my_pow(x, y - 1)

x = int(input())
y = int(input())
off = int(input())

result = str(my_pow(x, y))
result = result[:off]
result = hex(int(result))
result = result[2:]
result = result.upper()

print(result)
