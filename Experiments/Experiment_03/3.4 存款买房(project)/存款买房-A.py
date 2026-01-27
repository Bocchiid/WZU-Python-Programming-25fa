import math


total_cost = float(input())           # '请输入总房价：'total_cost为当前房价
annual_salary = float(input())        # '请输入年薪：'
portion_saved = float(input()) / 100  # '请输入月存款比例：'月存款比例，输入30转为30%

# 根据首付款比例计算首付款金额和每个月需要存款数额
# 补充你的代码
portion_down_payment = 0.30

down_payment = total_cost * portion_down_payment
monthly_deposit = annual_salary / 12 * portion_saved

print(f'首付 {down_payment:.2f} 元', )
print(f'月存款 {monthly_deposit:.2f} 元')

# 计算多少个月才能存够首付款，结果为整数，不足1月按1个月计算，即向上取整
# 补充你的代码
number_of_months = down_payment / monthly_deposit

print(f'需要{math.ceil(number_of_months)}个月可以存够首付')
