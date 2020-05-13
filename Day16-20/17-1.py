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


def bubble_sort_new(items, comp=lambda x, y: x > y):
    """ 搅拌排序(冒泡排序升级版) """
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def merge(items, items, comp=lambda x, y: x < y):
    """ 合并(将两个有序的列表合并成一个有序的列表) """
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """ 归并排序 """
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def seq_search(items, key):
    """ 顺序查找 """
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """ 折半查找 """
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    ss = select_sort([24, 25, 23, 55, 32, 44])
    bs = bubble_sort([24, 25, 23, 55, 32, 44])
    bsn = bubble_sort_new([24, 25, 23, 55, 32, 44])
    print(ss)
    print(bs)
    print(bsn)
