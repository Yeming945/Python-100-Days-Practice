"""
算法：解决问题的方法和步骤
评价算法的好坏：渐近时间复杂度和渐近空间复杂度。
渐近时间复杂度的大O标记：
- 常量时间复杂度 - 布隆过滤器 / 哈希存储
- 对数时间复杂度 - 折半查找（二分查找）
- 线性时间复杂度 - 顺序查找 / 计数排序
- 对数线性时间复杂度 - 高级排序算法（归并排序、快速排序）
- 平方时间复杂度 - 简单排序算法（选择排序、插入排序、冒泡排序）
- 立方时间复杂度 - Floyd算法 / 矩阵乘法运算
- 几何级数时间复杂度 - 汉诺塔
- 阶乘时间复杂度 - 旅行经销商问题 - NPC 
"""

# 排序算法(选择, 冒泡和归并) 和查找算法(顺序和折半)


def select_sort(items, comp=lambda x, y: x > y):
    """ 简单选择排序 """
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

    return items


def bubble_sort(items, comp=lambda x, y: x > y):
    """ 冒泡排序 """
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


if __name__ == "__main__":
    ss = select_sort([24, 25, 23, 55, 32, 44])
    bs = bubble_sort([24, 25, 23, 55, 32, 44])
    print(ss)
    print(bs)
