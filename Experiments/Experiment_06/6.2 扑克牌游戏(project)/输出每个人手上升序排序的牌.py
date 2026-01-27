import random

def sort_cards(person, m):
    """对m个人手上的牌进行升序排序，花色按黑红梅方，牌面按点数，大王最大，小王第二大"""
    ########## Begin ##########
    desigh_dir = {'♠': 0, '♥': 1, '♣': 2, '♦': 3, 'j': 13, 'J':14}
    num_dir = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4,'7': 5,
               '8': 6, '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11,
               'A': 12, 'okers': 13, 'OKERS': 14}

    for i in range(m):
        person[i] = sorted(person[i], key = lambda x: (desigh_dir[x[0]], num_dir[x[1:]]))

    return person
    ########## End ##########

def start():
    """初始顺序，返回元素为字符串的列表"""
    cards_start = [i + j for i in desigh for j in num] + ghost
    return cards_start

def shuffle_cards(cards_start):
    """打乱顺序，返回元素为字符串的列表"""
    random.shuffle(cards_start)
    return cards_start

def traver(cards_shuffle, m):
    """发牌给m个人,返回二维列表"""
    person = []
    for i in range(m):
        person.append(cards_shuffle[i::m])
    return person

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
    cards_sort = sort_cards(cards_n, n)
    print('每个人手上排序的牌')
    for i in range(n):
        print(*cards_sort[i])
