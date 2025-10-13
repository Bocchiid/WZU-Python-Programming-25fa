def start():
    """初始顺序，返回元素为字符串的列表"""
    ########## Begin ##########
    res = []

    for i in desigh:
        for j in num:
            res.append(i + j)

    for i in ghost:
        res.append(i);

    return res;
    ########## End ##########

if __name__ == '__main__':
    desigh = ['♠', '♥', '♣', '♦']  # 表示黑桃、红桃、梅花、方块
    num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ghost = ['jokers', 'JOKERS']
    cards = start()
    print('新牌顺序')
    print(*cards)
