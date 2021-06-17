#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 17:57
# @Author  : sakura
# @Site    : 二分查找的变种问题1
# @File    : findFirstValue.py
# @Software: PyCharm

"""查找第一个值等于给定值的元素"""


def findFirsrVar(data, target):
    """
    在有重复元素的有序数组中查找以一个出现该元素的位置
    :param data:
    :param target:
    :return:
    """
    low, high = 0, len(data) - 1

    while low <= high:
        mid = low + (high - low >> 1)
        if target > data[mid]:
            low = mid + 1
        elif target < data[mid]:
            high = mid - 1
        else:  # 等于的情况 需要再讨论
            # 1. 如果刚好定位到data[0] 那肯定ok
            # 2. 如果mid前面的元素 不等于data[mid]   也ok
            if mid == 0 or data[mid - 1] != target:
                return mid
            else:
                # 否则  前面的元素还等于 target    应该再向前走
                high = mid - 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 8, 8, 8, 8, 12, 45, 78, 89, 99, 99, 99, 123, 234, 465, 456]
    print(findFirsrVar(data, 8))  # 结果应该是 5
    print(findFirsrVar(data, 99))  # 结果应该是  13
