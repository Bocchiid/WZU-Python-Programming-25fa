def days_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，计算这个日期中的月份有多少天？返回值为整型，
    表示当前月份天数。
    @参数 current_date：表示日期，字符串类型
    """
    # 补充你的代码 
    month = int(current_date[4:6])
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap(current_date):
        list[1] = 29

    return list[month - 1]

def leap(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判断这个日期中的年份是否为闰年
    返回值为布尔型。
    闰年的判定方法是：能被400整除或能被4整除且同时不能被100整除的是闰年。
    """
    # 补充你的代码
    year = int(current_date[:4])

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True

    return False

if __name__ == '__main__':
    CurrentDate = input()
    days = days_of_month(CurrentDate)
    print(f'{CurrentDate[:4]}年{int(CurrentDate[4:6])}月有{days}天')
