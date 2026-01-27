# 请补充你的代码

buy_in = float(input("请输入股票的买入价格（每股）："))
sell_out = float(input("请输入股票的卖出价格（每股）："))
number = int(input("请输入持有的股票数量："))

total_interest = (sell_out - buy_in) * number

print(f'总收益为：{total_interest:.2f} 元')
