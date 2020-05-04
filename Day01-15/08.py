from time import sleep
from math import sqrt


class Clock(object):
    """ 数字时钟 """
    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param: hour:时
        :param: minute:分
        :param: second:秒
         """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """ 走字 """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """ 显示时间 """
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def case1():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


class Point(object):
    def __init__(self, x=0, y=0):
        """初始化方法
        :param: x:横坐标
        :param: y:纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx**2 + dy**2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def case2():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    # case1()
    case2()
