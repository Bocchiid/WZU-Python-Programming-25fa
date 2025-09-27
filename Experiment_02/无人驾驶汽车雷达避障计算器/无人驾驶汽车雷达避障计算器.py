# 提示用户输入当前速度
velocity = float(input("请输入当前速度（米/秒）："))
# 补充代码提示用户输入障碍物距离
distance_to_obstacle = float(input('请输入障碍物距离（米）：'))
# 补充代码提示用户输入车辆最大制动加速度
max_deceleration = float(input('请输入车辆最大制动加速度（米/秒²）：'))

# 计算车辆完全停止前需要的制动距离
braking_distance = (velocity ** 2) / (2 * max_deceleration)

print(f"制动距离为：{braking_distance:.2f} 米")
# 比较比较制动距离是否大于障碍物距离，判断是否会发生碰撞并输出结果
if (braking_distance > distance_to_obstacle): # 补充判断会相撞的条件代码，输出碰撞警告信息
    print(f'警告：车辆将会撞上障碍物！') # 补充提示信息
else:
    print(f"安全：车辆不会撞上障碍物。")
