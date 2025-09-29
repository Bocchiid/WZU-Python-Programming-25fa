def income_tax():
    """用户输入应发工资薪金所得、五险一金金额和个税免征额，输出应缴税款和实发工资，
    结果保留小数点后两位。当输入数字小于0 或等于0 时，输出“error”。
    实发工资 = 应发工资 - 五险一金 - 个人所得税
    建议使用以下变量名：
    salary：每月应发工资薪金
    insurance_fund：五险一金
    exemption：个税免征额
    educted_amount：速算扣除数
    测试用例
    输入（冒号前是提示性文字，冒号后的数字为用户输入）
    请输入应发工资薪金金额：16000
    请输入五险一金金额：4000
    请输入个税免征额：5000
    输出
    应缴税款490.00 元，实发工资11510.00 元。
    """
    # ====================Begin===================================
    salary = float(input())
    insurance_fund = float(input())
    exemption = float(input())

    if (salary <= 0 or insurance_fund <= 0 or exemption <= 0):
        print('error')
    else:
        taxable = salary - insurance_fund - exemption
        tax_rate, educted_amount = 0, 0

        if (taxable < 0):
            taxable = 0
            tax_rate = 0
            educted_amount = 0
        elif (taxable <= 3000):
            tax_rate = 0.03
            educted_amount = 0
        elif (taxable <= 12000):
            tax_rate = 0.1
            educted_amount = 210
        elif (taxable <= 25000):
            tax_rate = 0.2
            educted_amount = 1410
        elif (taxable <= 35000):
            tax_rate = 0.25
            educted_amount = 2660
        elif (taxable <= 55000):
            tax_rate = 0.3
            educted_amount = 4410
        elif (taxable <= 80000):
            tax_rate = 0.35
            educted_amount = 7160
        else:
            tax_rate = 0.45
            educted_amount = 15160

        tax = taxable * tax_rate - educted_amount
        true_salary = salary - insurance_fund - tax

        print(f'应缴税款{tax:.2f}元，实发工资{true_salary:.2f}元。')
    # ======================End=================================
if __name__ == '__main__':
    income_tax()              # 调用函数完成计算和输出
