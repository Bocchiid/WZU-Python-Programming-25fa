def say_hi_multi_parameter(*list):    # 括号里用合适的对象替换“传入参数”
    # 补充你的代码
    for name in list:
        print(f'{name}，你好！')


#调用say_hi_multi_parameter并传入参数
say_hi_multi_parameter('孟浩然')
say_hi_multi_parameter('杜甫', '李白', '柳宗元', '李商隐')
