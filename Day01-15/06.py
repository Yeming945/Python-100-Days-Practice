from random import randint


def practice1():
    """ 输入M和N计算C(M,N) """
    m = int(input('m= '))
    n = int(input('n= '))
    fm = 1
    for num in range(1, m + 1):
        fm *= num
    fn = 1
    for num in range(1, n + 1):
        fn *= num
    fm_n = 1
    for num in range(1, m - n + 1):
        fm_n *= num
    print(fm // fn // fm_n)


def practice2():
    """ 求阶乘 """
    def fac(num):
        result = 1
        for n in range(1, num + 1):
            result *= n
        return result

    m = int(input('m= '))
    n = int(input('n= '))
    print(fac(m) // fac(n) // fac(m - n))


def practice3():
    """ 摇色子 """
    def roll_dice(n=2):
        total = 0
        for _ in range(n):
            total += randint(1, 6)
        return total

    def add(a=0, b=0, c=0):
        """ 三个数相加 """
        return a + b + c

    # 如果没有指定参数那么使用默认值摇两颗色子
    print(roll_dice())
    # 摇三颗色子
    print(roll_dice(3))
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    # 传递参数时可以不按照设定的顺序进行传递
    print(add(c=50, a=100, b=200))


def practice4():
    """ 实现任意数量的加法 """
    def add(*args):
        # 在参数名前面加*表示args是一个可变参数
        total = 0
        for val in args:
            total += val
        return total

    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(1, 3, 5, 7, 9))


def practice5():
    def gcd(x, y):
        """ 求最大公约数 """
        (x, y) = (y, x) if x > y else (x, y)
        for factor in range(x, 0, -1):
            if x % factor == 0 and y % factor == 0:
                return factor

    def lcm(x, y):
        """ 求最小公倍数 """
        return x * y // gcd(x, y)


def is_palindrome(num):
    """ 判断一个数是不是回文数 """
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num


def is_prime(num):
    """ 实现判断一个数是不是素数的函数 """
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == "__main__":
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
    else:
        print('No!')
# practice1()
# practice2()
# practice3()
# practice4()
# practice5()
