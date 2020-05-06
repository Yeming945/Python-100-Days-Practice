import time
from math import sqrt


def main():
    f = open('致橡树.txt', 'r', encoding='utf-8')
    print(f.read)
    f.close()


def main2():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read)
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except lookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


def main3():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except lookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def main4():
    # 一次读取整个文件内容
    with open('致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    with open('致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('致橡树.txt') as f:
        lines = f.readlines()
    print(lines)


def is_prime(n):
    """ 判断素数的函数 """
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main5():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')


def main6():
    """ 读取二进制文件 """
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))  # class 'bytes

        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)

    except FileNotFoundError as e:
        print('指定的文件无法打开!')
    except IOError as e:
        print('读写文件时出现错误!')
    print('程序执行结束!')


if __name__ == "__main__":
    # main()
    # main2()
    # main3()
    # main4()
    # main5()
    main6()
