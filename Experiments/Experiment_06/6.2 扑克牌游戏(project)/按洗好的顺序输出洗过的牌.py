import random

def shuffle_cards(cards_start):
    """打乱顺序，返回元素为字符串的列表"""
    ########## Begin ##########
    random.shuffle(cards_start)

    return cards_start
    ########## End ##########

def start():
    """初始顺序，返回元素为字符串的列表"""
    cards_start = [i + j for i in desigh for j in num] + ghost
    return cards_start

if __name__ == '__main__':
    desigh = ['♠', '♥', '♣', '♦']  # 表示黑桃、红桃、梅花、方块
    num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    ghost = ['jokers', 'JOKERS']
    s = int(input())
    random.seed(s)
    cards = start()
    cards_after = shuffle_cards(cards)
    print('洗牌顺序')
    print(*cards_after)
