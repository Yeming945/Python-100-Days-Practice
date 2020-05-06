from math import sqrt
from time import time, localtime, sleep


class Person1(object):
    """ @property装饰器 """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def case1():
    person = Person1('王大锤', 12)
    person.play()
    person.age = 22
    person.play()


class Person2(object):
    # 限定Person对象只能绑定_name, _age和_gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def case2():
    person = Person2('王大锤', 12)
    person.play()
    person._gender = '男'


class Triangle(object):
    def __init__(self, a, c, b):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_vaild(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) *
                    (half - self._c))


def case3():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用的
    if Triangle.is_vaild(a, c, b):
        t = Triangle(a, b, c)
        print(t.perimeter())
        # 也可以通过给类发消息来调用对象方法
        # 方式要传入接收消息的对象作为参数
        print(Triangle.perimeter(t))
        print(t.area())
    else:
        print('无法构成三角形.')


class Clock(object):
    """ 数字时钟 """

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """ 走字 """
        self._second += 1
        if self._second == 60:
            self._second == 0
            self._minute += 1
            if self._minute == 60:
                self._minute == 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """ 显示时间 """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def case4():
    # 通过类方法创建对象并获取系统时间
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == "__main__":
    # case1()
    # case2()
    # case3()
    case4()
