import random

def person_name(gender_of_id, last_name_file, male_name_file, female_name_file):
    """
    @参数 gender_of_id：性别，字符串类型
    @参数 last_name_file：百家姓文件名，字符串类型
    @参数 male_name_file：男性常用名文件名，字符串类型
    @参数 female_name_file：女性常用名文件名，字符串类型
    接收性别、百家姓文件名、男性常用名文件名、女性常用名文件名为参数
    先随机抽取一个姓氏，再根据性别随机抽取名字，
    返回表示姓名的字符串。
    """
    #####################Begin#####################################
    with open(last_name_file, 'r', encoding='utf-8') as data:
        last = [line.strip().replace('，', '').replace('。', '')
                for line in data]

    last1 = ''.join(last[:51])
    last2 = ''.join(last[51:])
    last = list(last1) + [last2[i * 2: i * 2 + 2] for i in range(len(last2) // 2)]  # 得到姓的列表

    last_name_selected = random.choice(last)

    if gender_of_id == '男':
        gender_name_file = male_name_file
    else:
        gender_name_file = female_name_file

    with open(gender_name_file, 'r', encoding = 'utf-8') as f:
        first_name = f.read().strip().split()

    first_name_selected = random.choice(first_name)

    return last_name_selected + first_name_selected
    #####################End#####################################


def judge(txt):
    """接收一个字符串为参数.
    如果参数值为“性别”，输出当前模拟身证上的性别；
    如果参数值为“姓名”，输出当前模拟身证上的姓名。"""
    if txt == '姓名':
        print(person)
    elif txt == '性别':
        print(user_gender)
    else:
        print('输入错误')


if __name__ == '__main__':
    last_name_filename = 'data/family names.txt'    # 百家姓
    male_name_filename = 'data/popularNameM.txt'    # 男性名来源文件
    female_name_filename = 'data/popularNameF.txt'  # 女性名来源文件
    random.seed(int(input()))                       # 随机数种子，不用于自动评测时注释掉此行
    user_gender = random.choice('男女')               # 随机生成男或女
    person = person_name(user_gender, last_name_filename, male_name_filename, female_name_filename)  # 根据性别生成人名
    text = input()
    judge(text)
