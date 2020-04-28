import random
from math import sqrt


def pratice1():
    """ 用for循环实现1-100求和 """
    sum = 0
    for i in range(101):
        sum += i
    print(sum)


def pratice2():
    """ 用for循环实现1-100之间的偶数求和 """
    sum = 0
    for i in range(2, 101, 2):
        sum += i
    print(sum)


def pratice3():
    """ 猜数字游戏 """
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')


def pratice4():
    """ 输入一个正整数判断它是不是素数 """
    num = int(input('请输入一个正整数: '))
    end = int(sqrt(num))
    is_prime = True
    for i in range(2, end + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)


def pratice5():
    """ 输入两个正整数, 计算它们的最大公约数和最小公倍数 """
    x = int(input('x= '))
    y = int(input('y= '))
    # 如果x大于y就交换x和y的值
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            print('%d和%d的最大公约数是%d' % (x, y, factor))
            print('%d和%d的最小公约数是%d' % (x, y, x * y // factor))
            break


def pratice6():
    """ 打印三角形图案 """
    row = int(input('请输入行数: '))
    for i in range(row):
        for _ in range(i + 1):
            print('*', end='')
        print()

    for i in range(row):
        for j in range(row):
            if j < row - i - 1:
                print('', end='')
            else:
                print('*', end='')
        print()

    for i in range(row):
        for _ in range(row - i - 1):
            print(' ', end='')
        for _ in range(2 * i + 1):
            print('*', end='')
        print()


# pratice1()
# pratice2()
# pratice3()
# pratice4()
# pratice5()
# pratice6()
