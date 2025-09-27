python = 3
math = 4
english = 4
physical_education = 2
military_theory = 2
philosophy = 2
# 补充你的代码

tuition_per_credit = eval(input('请输入每学分学费金额：'))

total_credits = python + math + english + physical_education + military_theory + philosophy
total_tuition = total_credits * tuition_per_credit

living_expenses = eval(input('请输入你每个月生活费：'))

total_cost = 5 * living_expenses + total_tuition
student_loan = total_cost * 0.6

print(f'本学期你能够贷款{student_loan:.2f}元')
