from random import randint


def practice1():
    """ 寻找水仙花数 """
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10
        high = num // 100
        if num == low**3 + mid**3 + high**3:
            print(num)


def practice2():
    """ 正整数的翻转 """
    num = int(input('num= '))
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    print(reversed_num)


def practice3():
    """ 百钱百鸡问题
    百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
    鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。
    百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
    翻译成现代文是：公鸡5元一只，母鸡3元一只，
    小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？ """
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * 3 + 3 * y + z / 3 == 100:
                print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))


def practice4():
    """ Craps赌博游戏 """
    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if 0 < debt <= money:
                break

        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜!')
                money -= debt
            elif current == first:
                print('玩家胜!')
                money += debt
            else:
                needs_go_on = True
    print('你破产了, 游戏结束!')


# practice1()
# practice2()
# practice3()
# practice4()
