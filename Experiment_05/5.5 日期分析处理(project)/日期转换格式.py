def separate_date(current_date, symbol):
    """接收一个用8个字符表示日期的字符串和一个符号为参数，返回用该符号分隔的日期，字符串类型。
    @参数 current_date：表示日期，字符串类型
    @参数 symbol：分隔符号，字符串类型
    例如传入'20201031'和"/",返回字符串'2020/09/09'
    """
    # 补充你的代码
    year = current_date[:4]
    month = current_date[4:6]
    day = current_date[6:]

    format_string = year + symbol + month + symbol + day

    return format_string

if __name__ == '__main__':
    CurrentDate = input()  # 输入8位数字表示的日期
    sign = input()         # 输入分隔符
    print(separate_date(CurrentDate, sign))  # 输出用分隔符分隔的日期
