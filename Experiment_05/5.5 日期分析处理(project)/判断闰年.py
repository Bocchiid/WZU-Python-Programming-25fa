def leap(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判断这个日期中的年份是否为闰年
    返回值为布尔型。
    闰年的判定方法是：能被400整除或能被4整除且同时不能被100整除的是闰年。
    """
    # 补充你的代码
    year = int(current_date)

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True

    return False

if __name__ == '__main__':
    date = input()      # 输入一个表示年份的8位数字字符串
    if leap(date[:4]):  # 如果输入的年份是闰年
        print(f'{date[:4]}年是闰年')
    else:
        print(f'{date[:4]}年不是闰年')
