# coding = utf-8


def cut(string, char):
    """
    Cut函数
    以 char 分割 string 并添加“幻塔”
    char: 分割字符
    string: 待处理的字符串
    """
    index = 0
    string_list = string.split(char)
    while 1:
        if string_list[0] == string_list[-1]:
            if '幻塔' not in string_list[0]:
                string_list[index] = string_list[index] + '幻塔'
            break
        if string_list[index] != string_list[-1]:
            if '原神' not in string_list[index] \
                    and '幻塔' not in string_list[index]:
                string_list[index] = string_list[index] + '幻塔'
        else:
            break
        index += 1
    string = char.join(string_list)
    return string


def exchange(string):
    """
    Exchange函数
    将原神的评论转变为幻塔的评论
    string: 待处理的字符串
    """

    # import re  我再也不需要re模块了，哈哈

    import jieba

    # 开始在断句的前面添加“幻塔”
    string = string.rstrip('，。？！')  # 去除结尾的标点符号，方便处理
    string = cut(string, '，')  # 处理逗号
    string = cut(string, '。')  # 处理句号
    string = cut(string, '？')  # 处理问号
    string = cut(string, '！')  # 处理叹号

    # string = re.sub('原神', '幻塔', string)  # 替换“原神”为“幻塔”
    '''
    注意上面的注释句子，本来是用于替换原神为幻塔的代码，但是废弃了，为什么呢？给你个句子，自己体会：
    秦始皇派蒙恬还原神舟六号工程。（注意第7个字符后的那个词）
    以上的代码将使用 jieba 模块进行自然语言处理。
    '''

    m_index = 0
    exchange_list = list(
        jieba.cut(string, cut_all=False)  # 使用精确断句，否则就白干了
    )

    while 1:
        if exchange_list[m_index] == '原神':
            exchange_list[m_index] = '幻塔'
        elif exchange_list[m_index] is exchange_list[-1]:
            break
        elif m_index == 2147483647:  # 我可不想遇到死循环，差不多得了
            break
        m_index += 1
    string = ''.join(exchange_list)  # 空字符连接
    return string + '，。'


if __name__ == '__main__':  # 主程序，tnnd，为什么不运行，运行，运行啊！！！
    keyboard = input('请输入：')
    print('=====制造程序开始运行=====')
    output = exchange(keyboard)
    print('=====制造程序运行完毕=====')
    print('\n输出：' + output)
    input('按回车键继续...')
