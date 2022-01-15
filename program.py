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
    import re  # 我需要re模块来进行操作qwq

    # 开始在断句的前面添加“幻塔”
    string = string.rstrip('，。？！')  # 去除结尾的标点符号
    string = cut(string, '，')  # 处理逗号
    string = cut(string, '。')  # 处理句号
    string = cut(string, '？')  # 处理问号
    string = cut(string, '！')  # 处理叹号
    string = re.sub('原神', '幻塔', string)  # 替换“原神”为“幻塔”
    return string + '，。'


if __name__ == '__main__':
    keyboard = input('请输入：')
    print('\n输出：' + exchange(keyboard))
    input('按回车键继续...')
