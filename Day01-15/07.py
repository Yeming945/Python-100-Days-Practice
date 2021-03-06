import os
import time
import random
from random import randint, sample


def practice1():
    """ 练习1：在屏幕上显示跑马灯文字。 """
    def main():
        content = '北京欢迎你为你开天辟地…………'
        while True:
            # 清理屏幕上的输出
            os.system('cls')
            print(content)
            # 休眠200毫秒
            time.sleep(0.2)
            content = content[1:] + content[0]

    main()


def generate_code(code_len=4):
    """
    练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def get_suffix(filename, has_dot=False):
    """
    获取文件的后缀名
    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
      """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(x):
    m1, m2 = (x[0], x[1] if x[0] > x[1] else (x[1], x[0]))
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def practice5():
    """ 计算指定的年月日是这一年的第几天 """
    def is_leap_year(year):
        """ 判断指定的年份是不是闰年
        :param: year:年份
        :return: 闰年返回True平年返回False
         """
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

    def which_day(year, month, date):
        """
        计算传入的日期是这一年的第几天
        :param: year:年
        :param: month:月
        :param: date:日
        :return: 第几天
        """
        days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30,
                          31]][is_leap_year(year)]
        total = 0
        for index in range(month - 1):
            total += days_of_month[index]
        return total + date

    def main():
        print(which_day(1980, 11, 28))
        print(which_day(1981, 2, 18))
        print(which_day(2018, 1, 8))
        print(which_day(2020, 4, 29))

    main()


def practice6():
    """ 打印杨辉三角 """
    def main():
        num = int(input('Number of rows: '))
        yh = [[]] * num
        for row in range(len(yh)):
            yh[row] = [None] * (row + 1)
            for col in range(len(yh[row])):
                if col == 0 or col == row:
                    yh[row][col] = 1
                else:
                    yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
                print(yh[row][col], end='\t')
            print()

    main()


def case1():
    def display(balls):
        """
        输出列表中的双色球号码
        """
        for index, ball in enumerate(balls):
            if index == len(balls) - 1:
                print('|', end=' ')
            print('%02d' % ball, end=' ')
        print()

    def random_select():
        """ 随机选择一组号码 """
        red_balls = [x for x in range(1, 34)]
        selected_balls = []
        selected_balls = sample(red_balls, 6)
        selected_balls.sort()
        selected_balls.append(randint(1, 16))
        return selected_balls

    def main():
        n = int(input('机选几注: '))
        for _ in range(n):
            display(random_select())

    main()


def case2():
    """ 约瑟夫环问题 """
    def main():
        persons = [True] * 30
        counter, index, number = 0, 0, 0
        while counter < 15:
            if persons[index]:
                number += 1
                if number == 9:
                    persons[index] = False
                    counter += 1
                    number = 0
            index += 1
            index %= 30
        for person in persons:
            print('基' if person else '非', end='')

    main()


def case3():
    def print_board(board):
        print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
        print('-+-+-')
        print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
        print('-+-+-')
        print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

    def main():
        init_board = {
            'TL': ' ',
            'TM': ' ',
            'TR': ' ',
            'ML': ' ',
            'MM': ' ',
            'MR': ' ',
            'BL': ' ',
            'BM': ' ',
            'BR': ' ',
        }

        begin = True
        while begin:
            curr_board = init_board.copy()
            begin = False
            turn = 'x'
            counter = 0
            os.system('clear')
            print_board(curr_board)
            while counter < 9:
                move = input('轮到%s走棋, 请输入位置: ' % turn)
                counter += 1
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
                os.system('clear')
                print_board(curr_board)
            choice = input('再玩一局?yes|no')
            begin = choice == 'yes'

    main()


if __name__ == "__main__":
    # practice1()
    # generate_code()
    # print(get_suffix('test111.txt', False))
    # practice5()
    # practice6()
    # case1()
    # case2()
    case3()
