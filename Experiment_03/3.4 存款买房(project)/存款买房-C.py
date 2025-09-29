def format(current_savings):
    current_savings = int(current_savings + 0.5)
    current_savings = str(current_savings)

    ret = ''

    for i in range(len(current_savings)):
        if (len(current_savings) - i) % 3 == 0 and i != 0:
            ret += ','

        ret += current_savings[i]

    return ret

total_cost = float(input())           # total_cost为当前房价
annual_salary = float(input())        # 年薪
portion_saved = float(input()) / 100  # 月存款比例，输入30转为30%
semi_annual_raise = float(input()) /100     # 输入每半年加薪比例，输入7转化为7%

portion_down_payment = 0.3                         # 首付比例，浮点数
down_payment = portion_down_payment * total_cost   # 首付款
print(f'首付 {down_payment:.2f} 元')

current_savings = 0                                # 存款金额，从0开始
number_of_months = 0
# 补充你的代码，计算月工资，计算月存款
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

# 补充你的代码，计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整

interest_rate = 0.0225

while current_savings < down_payment:
    number_of_months += 1
    current_savings += current_savings * interest_rate / 12
    current_savings += monthly_saved

    if number_of_months % 6 == 0:
        monthly_saved *= 1 + semi_annual_raise

    if number_of_months % 12 == 0:
        print(f'第{number_of_months}个月月末有{format(current_savings)}元存款')

print(f'需要{number_of_months}个月可以存够首付')
