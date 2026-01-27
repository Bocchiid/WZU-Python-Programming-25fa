python = 3
math = 4
english = 4
physical = 2
military_theory = 2
philosophy = 2
# 补充你的代码

pre_cost = int(input())

credits = python + math + english + physical + military_theory + philosophy
total_cost = pre_cost * credits

print(f'你本学期选修了{credits}个学分。')
print(f'你应缴纳的学费为{total_cost}元。')
