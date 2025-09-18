# 请补充你的代码

weight = float(input("请输入您的体重（公斤）："))
height = float(input("请输入您的身高（米）："))

bmi = weight / (height * height)

print(f"您的BMI值为：{bmi:.2f}")

if (bmi < 18.5):
    print("体重过轻")
elif (18.5 <= bmi <= 24.9):
    print("体重正常")
elif (25 <= bmi < 29.9):
    print("体重超重")
else:
    print("肥胖")
