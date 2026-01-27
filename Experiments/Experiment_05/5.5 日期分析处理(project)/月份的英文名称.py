def name_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，返回这个月份对应的英文单词及其缩写形式。
    @参数 current_date：表示日期，字符串类型
    例如：current_date为20201031，返回值为'October','Oct.'
    日期的英文全称：['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    日期的英文缩写：September为前四位字母加点，其余月份均为前三位字母加点，如：'Sept.','Jan.'
    """
    # 补充你的代码
    month = int(current_date[4:6])
    list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']

    name_of_month = list[month - 1]

    if month == 9:
        abbr_of_month = name_of_month[:4]
    else:
        abbr_of_month = name_of_month[:3]

    abbr_of_month += '.'
        
    return name_of_month, abbr_of_month

if __name__ == '__main__':
    CurrentDate = input()
    monthName, monthAbbr = name_of_month(CurrentDate)  # 获得月份名称和缩写
    print(f'{int(CurrentDate[4:6])}月英文是{monthName}，缩写为{monthAbbr}')
