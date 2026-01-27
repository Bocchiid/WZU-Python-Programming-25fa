def get_guessed_word(cover_word, word, letter):
    """接受三个字符串为参数：分别表示正在猜测的遮盖了字母的单词、随机抽取的单词和正在猜测的字母。
    每次猜测后产生一个由猜中字母和下划线与空格组成的字符串，猜中的字母显示出来，未知字母用"_"
    表示，字母间留一个空格。返回每次猜测后由字母和下划线组成的字符串。
    @参数 cover_word：遮盖了字母的单词，字符串类型
    @参数 word：随机抽取的单词，字符串类型
    @参数 letter：正在猜测的字母，字符串类型
    """
    # 补充你的代码
    new_cover_word = ''

    for i in range(len(word)):
        if word[i] == letter:
            new_cover_word += letter
        else:
            new_cover_word += cover_word[i * 2]

        new_cover_word += ' '

    cover_word = new_cover_word

    print(f'当前猜测结果为：{cover_word}')
    return cover_word

if __name__ == '__main__':
    word = input()
    print(f'单词长度为{len(word)}')  # 先提示用户单词长度
    cover_word = '_ ' * len(word)  # 产生一个由下划线与空格构成的字符串，每组下划线与空格代表一个字母
    print(cover_word)
    for i in range(1, 2 * len(word) + 1):  # 最多猜测2倍字母数次
        print(f'当前是第{i}次猜测，你还有{2 * len(word) - i}次机会')
        letter = input('请输入你猜测的字母：')  # 输入猜测的字母
        cover_word = get_guessed_word(cover_word, word, letter)
        guess_word = cover_word.replace(' ', '')
        if guess_word == word:  # 替换字符串中的空格，查看是否猜中
            print(f'你太厉害了，居然只用了{i}次就猜中了单词')
            print(f'秘密单词是：{guess_word}')  # 猜中后输出时去掉单词中的空格
            break
