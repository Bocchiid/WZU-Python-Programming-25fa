import random

def traver(cards_shuffle, m):
    """发牌给m个人,返回二维列表"""
    ########## Begin ##########
    res = [[] for _ in range(m)]
    total = len(cards_shuffle)
    length = total // m
    count = 0

    for i in range(length):
        for each in res:
            each.append(cards_shuffle[count])
            count += 1
            
            if count == total:
                break

    return res
    ########## End ##########

def start():
    """初始顺序，返回元素为字符串的列表"""
    cards_start = [i + j for i in desigh for j in num] + ghost
    return cards_start

def shuffle_cards(cards_start):
    """打乱顺序，返回元素为字符串的列表"""
    random.shuffle(cards_start)
    return cards_start

if __name__ == '__main__':
    desigh = ['♠', '♥', '♣', '♦']  # 表示黑桃、红桃、梅花、方块
    num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ghost = ['jokers', 'JOKERS']
    n = int(input())  # 输入参与游戏的人数
    s = int(input())
    random.seed(s)
    print(f'参与游戏的人数：{n}')
    cards = start()
    cards_after = shuffle_cards(cards)
    cards_n = traver(cards_after, n)
    print('每个人手上分到的牌')
    for i in range(n):
        print(*cards_n[i])
