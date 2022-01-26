# coding = utf-8


def char_cut(string, char):
    """
    Cut函数
    以 char 分割 string 并添加“幻塔”
    char: 分割字符
    string: 待处理的字符串
    """
    index = 0
    string_list = string.split(char)
    for str_char in string_list:
        if '原神' not in str_char \
                and '幻塔' not in str_char:
            string_list[index] = string_list[index] + '幻塔'
        index += 1
    string = char.join(string_list)
    return string


def exchange(string):
    """
    Exchange函数
    将原神的评论转变为幻塔的评论
    string: 待处理的字符串
    """

    import jieba

    # 开始在断句的前面添加“幻塔”
    string = string.rstrip('，。？！')  # 去除结尾的标点符号，方便处理
    string = char_cut(string, '，')  # 处理逗号
    string = char_cut(string, '。')  # 处理句号
    string = char_cut(string, '？')  # 处理问号
    string = char_cut(string, '！')  # 处理叹号

    m_index = 0
    exchange_list = list(
        jieba.cut(string, cut_all=False)  # 使用精确断句，否则就白干了
    )

    # 以下句子停止使用while死循环，因为拥有了更好的解决方案
    for char in exchange_list:
        if char == '原神':
            exchange_list[m_index] = '幻塔'
        m_index += 1
    string = ''.join(exchange_list)  # 空字符连接
    return string + '，。'


if __name__ == '__main__':  # 主程序，tnnd，为什么不运行，运行，运行啊！！！
    keyboard = input('请输入：')
    print('\n=====制造程序开始运行=====\n')
    output = exchange(keyboard)
    print('\n=====制造程序运行完毕=====\n')
    print('输出：' + output)
    input('按回车键继续...')
