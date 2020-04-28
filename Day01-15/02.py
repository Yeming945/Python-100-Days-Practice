def practice1():
    """ 将华氏温度转为摄氏温度 """
    f = float(input('请输入华氏温度: '))
    c = (f - 32) / 1.8
    print(('%.1f华氏温度 = %.1f摄氏温度' % (f, c)))


def practice2():
    """ 计算半径圆的周长和面积 """
    pi = 3.1416
    radius = float(input('请输入圆的半径: '))
    perimeter = 2 * pi * radius
    area = pi * radius * radius
    print('周长: %.2f' % perimeter)
    print('面积: %.2f' % area)


def practice3():
    """ 输入年份, 如果是闰年输出True, 否则输出False """
    year = int(input('请出入年份: '))
    is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    print(is_leap)


# practice1()
# practice2()
# practice3()
