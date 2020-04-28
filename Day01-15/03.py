def practice1():
    """ 用户身份验证 """
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    if username == 'admin' and password == '123456':
        print('身份验证成功!')
    else:
        print('身份验证失败!')


def practice2():
    """ 英制单位英寸和公制单位厘米互换 """
    value = float(input('请输入长度: '))
    unit = input('请输入单位: ')
    if unit == 'in' or unit == '英寸':
        print('%f英寸 = %f厘米' % (value, value * 2.54))
    if unit == 'cm' or unit == '厘米':
        print('%f厘米 = %f英寸' % (value, value / 2.54))
    else:
        print('请输入有效的单位')


def practice3():
    """ 百分制成绩转换为等级制成绩
    要求：如果输入的成绩在90分以上（含90分）输出A；
    80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；
    60分-70分（不含70分）输出D；60分以下输出E。
    """
    score = float(input('请输入成绩: '))
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'
    print('对应的等级是:', grade)


def practice4():
    a = float(input('a= '))
    b = float(input('b= '))
    c = float(input('c= '))
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c))**0.5
        print('面积: %f' % (area))
    else:
        print('不能构成三角形!')


# practice1()
# practice2()
# practice3()
# practice4()
