import random
import datetime

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
    with open(last_name_file, 'r', encoding='utf-8') as data:
        last = [line.strip().replace('，', '').replace('。', '')
                for line in data]

    last1 = ''.join(last[:51])
    last2 = ''.join(last[51:])
    last = list(last1) + [last2[i * 2: i * 2 + 2] for i in range(len(last2) // 2)]  # 得到姓的列表
    last_name = random.choice(last)                                                 # 随机一个姓

    with open(male_name_file, 'r', encoding='utf-8') as data:
        male_name = data.readline().split()
    with open(female_name_file, 'r', encoding='utf-8') as data:
        female_name = data.readline().split()
    if gender_of_id == '男':
        first_name = random.choice(male_name)
    else:
        first_name = random.choice(female_name)
    return last_name + first_name


def area_code(area_file):
    """
    @参数 area_file：包含地区编码的文件名，字符串类型
    传入参数为包含地区编码和地区名的文件名的字符串，以地区编码为键，地区名为值构建字典作为返回值。
    """
    #####################Begin#####################################
    with open(area_file, 'r', encoding = 'utf-8') as f:
        lines = [line.strip().split(',') for line in f]

    dic = {}

    for key, value in lines:
        dic[key] = value

    return dic
    #####################End#####################################

def birthdate():
    """在1900-2020间随机抽取一个数字作为出生年份，再随机生成一个合法的包含月和日的日期。需
    要注意月份范围为1-12，1、3、5、7、8、10、12月的日期范围为1-31，4、6、9、11的日期范围为1-30，闰年2月
    的日期范围为1-29，平年2月的日期范围为1-28。年为4位字符串，月和日均为2位字符串，依序构成长
    度为8的字符串作为返回值，例如19840509 """
    year_of_birth = random.choice(range(1900, 2020))
    days_of_rand = datetime.timedelta(days=random.randint(1, 366))
    date_of_birth = datetime.datetime.strptime(str(year_of_birth)+'0101', "%Y%m%d") + days_of_rand          # 月份和日期项
    return date_of_birth.strftime("%Y%m%d")  # 19840509


def order_number(gender_of_id):
    """接收表示性别的字符串为参数，随机抽取1-99之间的整数作为生出顺序号，根据传入的性别随
    机抽取第17位序号数字，男性为偶数，女性为奇数。"""
    num = random.choice(range(1, 100))
    # gender_num = random.choice('13579') if gender_of_id == '男' else random.choice('02468')
    if gender_of_id == '男':
        gender_num = random.choice('13579')
    else:
        gender_num = random.choice('02468')

    return '{:02}'.format(num) + str(gender_num)


def id_of_17(area_of_code, birth_date, birth_order):
    """
    @参数 area_of_code：字符串
    @参数 birth_date：字符串
    @参数 birth_order：字符串
    接收地区码字典，出生日期和出生顺序号，随机抽取一个地区码，返回身份证号前17位的字符串。
    需要注意的是，抽取地区码时，要避免抽取到省或地级市的编码(最后2位编码为0)。
    """
    #####################Begin#####################################
    area_id = random.choice([x for x in area_of_code.keys() if x[-2:] != '00'])

    return area_id + birth_date + birth_order
    #####################End#####################################



def id17_to_18(id_number):
    """
    @ 参数 id_number：身份证号前17位，字符串
    为身份证号增加校验位，接收身份证号码前17位，返回18位身份证号，校验码的计算方法为：
    1. 将前面的身份证号码17位数分别乘以不同的系数。第一位到第十七位的系数分别为:
       7、9、10、5、8、4、2、1、6、3、7、9、10、5、8、4、2 ;
    2. 将这17位数字和系数相乘的结果相加;
    3. 用加出来和除以11，看余数是多少;
    4. 余数只可能有0、1、2、3、4、5、6、7、8、9、10这11个数字。
       其分别对应的最后一位身份证的号码为1、0、X、9、8、7、6、5、4、3、2，其中的X是罗马数字10;
    5. 通过上面得知如果余数是2，就会在身份证的第18位数字上出现罗马数字的Ⅹ；如果余数是10，
       身份证的最后一位号码就是2。
    """
    #####################Begin#####################################
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    res = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    sum_up = 0

    for i in range(len(id_number)):
        sum_up += int(id_number[i]) * factors[i]

    r = sum_up % 11

    return id_number + str(res[r])
    #####################End#####################################

def village_of_live(village_file, area_of_code):
    """
    @ 参数 village_file：包含常见小区名的文件名，字符串类型
    @ 参数 area_of_code：地区编码，字典类型
    从village_file中随机选择一个小区名，从area_of_code中随机选择一个地区编码，并从中获取省、市、
    县(区)名。楼栋号限制[1-30]中随机，单元号限制[1-7]中随机，楼层号限制[1-35]中随机，
    房间号限制[1-4]中随机。
    返回值为居住地址和地区编码，均为字符串类型。
    """
    with open(village_file, 'r', encoding='utf-8') as data:
        village_live = data.readline().split()
    village = random.choice(village_live)
    building = random.choice(range(1, 30))
    door = random.choice(range(1, 7))
    floor = random.choice(range(1, 35))
    room = random.choice(range(1, 4))
    area_id = random.choice([x for x in list(area_of_code.keys()) if x[-2:] != '00'])  # 避免抽到省市的编码
    #####################Begin#####################################
    province = area_of_code.get(area_id[:2]+'0000', '')
    city = area_of_code.get(area_id[:4]+'00', '')
    area = area_of_code[area_id]
    if area_id[:2] in ['11', '12', '31', '50']:          # 北京市，上海市，天津市，重庆市
        address_of_live = f'{province}{area}'
    else:
        address_of_live = f'{province}{city}{area}'
    address_of_live = address_of_live + f'{village}{building}栋{door}单元{floor:02}{room:02}室'
    return address_of_live, area_id
    #####################End#####################################


def all_of_nation(nation_file):
    """
    @参数 nation_file：文件名，字符串类型
    传入参数为包含民族的文件名，从中随机抽取一个民族为返回值。
    需要注意的是，返回值里不包含'族'字，例如抽取'蒙古族',返回值为'蒙古'。
    """
    #####################Begin#####################################
    with open(nation_file, 'r', encoding = 'utf-8') as f:
        text = f.read().strip().replace('族', '')

    ls = text.split()

    return random.choice(ls)
    #####################End#####################################


def judge(txt):
    """接收一个字符串为参数。
    如果参数值为“住址”，输出当前模拟身证上的住址；
    如果参数值为“身份证”，按身份证格式输出当前模拟身证上的全部信息；
    """
    if txt == '身份证号':
        print(id18)
    elif txt == '住址':
        print(address_and_code[0])
    else:
        print('输入错误')


if __name__ == '__main__':
    last_name_filename = 'data/family names.txt'  # 百家姓
    male_name_filename = 'data/popularNameM.txt'  # 男性名来源文件
    female_name_filename = 'data/popularNameF.txt'  # 女性名来源文件
    area_filename = 'data/IDcode.txt'  # 地区码
    village_filename = 'data/villageName.txt'  # 常用小区名
    nation_filename = 'data/nation.txt'  # 民族
    random.seed(int(input()))  # 随机数种子，不用于自动评测时注释掉此行
    user_gender = random.choice('男女')  # 随机生成男或女
    person = person_name(user_gender, last_name_filename, male_name_filename, female_name_filename)  # 根据性别生成人名
    area_number = area_code(area_filename)  # 地区编码，字典类型
    date = birthdate()  # 随机生日
    order = order_number(user_gender)  # 随机出生序号
    id17 = id_of_17(area_number, date, order)  # 拼接身份证号前17位
    id18 = id17_to_18(id17)  # 加校验码成18位身份证号
    address_and_code = village_of_live(village_filename, area_number)
    nationality = all_of_nation(nation_filename)
    text = input()
    judge(text)
