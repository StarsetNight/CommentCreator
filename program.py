# coding = utf-8

def str_insert(str_origin, pos, str_add):
    str_list = list(str_origin)  # 字符串转list
    str_list.insert(pos, str_add)  # 在指定位置插入字符串
    str_out = ''.join(str_list)  # 空字符连接
    return str_out


def exchange(string):
    """
    Exchange函数
    将原神的评论转变为幻塔的评论
    string: 待处理的评论
    """
    import re  # 我需要re模块来进行操作qwq
    string = re.sub('原神', '幻塔', string)
    if '，' not in string:  # 如果没有断句，则直接处理输出
        string = string + '幻塔，。'
        return string
    # 开始在断句的前面添加“幻塔”
    index = 0
    while 1:
        index += 1
        if string[index] == '，':
            string = str_insert(string, index, '幻塔')
            index += 2  # 防止死循环（刚才我已经TMD因为这个物理内存耗尽了，TNND，变量里全是“幻塔”两个字）
        elif string[index] == string[-1]:
            break
    string = string + '幻塔，。'
    return string


if __name__ == '__main__':
    keyboard = input('请输入：')
    print(exchange(keyboard))
    input('按回车键继续...')
