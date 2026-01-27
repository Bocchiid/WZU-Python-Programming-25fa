# read_file()函数帮助你读取文件到列表，直接调用就可以，此段不需修改
def read_file(filename):
    """接收一个文件名为参数，数据类型为字符串类型，文件编码为utf-8，
    返回值为列表，列表元素为将文件每一行根据逗号切分成的列表"""
    with open(filename, 'r', encoding='utf-8') as file:
        file_to_list = [line.strip().split(',') for line in file]
        # 文件全部内容读取出来放入列表中，每个元素为一行字符串
    return file_to_list  # 以列表形式返回文件中的数据


def student_id(ls_student, ls_school, ls_major):
    """参数为三个文件对象，依序分别由读学生信息、学院信息和专业信息文件获得。返回值为列表，为包含了新生成的学号的学生信息列表。"""
    dic_school = {x[0]: x[1] for x in ls_school}  # 构建学院字典
    dic_major = {x[0]: x[1] for x in ls_major}  # 构建专业字典
    student_detail = []
    ###########################Begin###########################
    dic_class = {x[4]: 1 for x in ls_student}

    for stu in ls_student:
        year = stu[5][-2:]
        school = dic_school[stu[2]]
        major = dic_major[stu[3]]
        Class = stu[4][-4:]

        rank = dic_class[stu[4]]
        dic_class[stu[4]] += 1

        student = '012' + year + school + major + Class + '{:02d}'.format(rank)
        stu.insert(0, student)

        student_detail.append(stu)
    ############################End############################
    return student_detail  # 返回加了学号的学生信息列表


def student_info(stu_name, ls_student):
    """参数为学生名字字符串和学生的信息列表，返回值为该学生的详细信息"""
    ###########################Begin###########################
    res = None

    for stu in ls_student:
        name = stu[1]

        if name == stu_name:
            res = stu

            break

    return res
    ############################End############################


def classmate(stu_class, ls_student):
    """参数为学生班级和学生信息列表，返回值为同班同学的信息列表"""
    ###########################Begin###########################
    ret_ls = []

    for stu in ls_student:
        Class = stu[5]

        if Class == stu_class:
            ret_ls.append(stu)

    return ret_ls
    ############################End############################


if __name__ == '__main__':
    stuName = input()  # 输入学生姓名
    stuClass = input()  # 输入班级
    student_list = read_file('step1/studentList.csv')[1:]  # 获得学生信息列表
    school_code = read_file('step1/schoolCode.csv')  # 获得学院信息列表
    major_code = read_file('step1/MajorCode.csv')  # 获得专业信息列表
    studentDetail = student_id(student_list, school_code, major_code)  # 调用函数计算ID并插入到列表中
    print(*student_info(stuName, studentDetail))  # 输出学生信息
    ls_classmate = classmate(stuClass, studentDetail)  # 返回同班同学信息列表
    for classmate in ls_classmate:  # 逐个输出同学信息
        print(*classmate)

