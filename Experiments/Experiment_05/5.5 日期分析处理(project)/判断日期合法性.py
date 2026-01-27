def legal_judge(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判定日期的合法性，返回值为布尔型。
    1，3，5，7，8，10，12月各31天，4，6，9，11各30天，闰年2月29天，平年2月28天。
    @参数 current_date：表示日期，字符串类型
    """
    # 补充你的代码
    month = int(current_date[4:6])
    day = int(current_date[6:])
    list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if leap(current_date):
        list[1] = 29

    if 1 <= day <= list[month - 1]:
        return True

    return False

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
    if legal_judge(CurrentDate):
        print(f'{CurrentDate}是合法日期')
    else:
        print(f'{CurrentDate}是非法日期')
