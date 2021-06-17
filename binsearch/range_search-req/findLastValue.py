#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 18:15
# @Author  : sakura
# @Site    : 
# @File    : findLastValue.py
# @Software: PyCharm

"""查找最后一个等于给定值的元素"""


def findLastVar(data, target):
    low, high = 0, len(data) - 1

    while low <= high:
        mid = low + (high - low >> 1)
        if target > data[mid]:
            low = mid + 1
        elif target < data[mid]:
            high = mid - 1
        else:  # 等于的情况 需要再讨论
            # 1. 如果刚好是最后一个值   ok
            # 2. 如果后一个元素不等于该值   也ok
            if mid == len(data) - 1 or data[mid + 1] != target:
                return mid
            else:
                # 否则 应该在往后继续找
                low = mid + 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 8, 8, 8, 8, 12, 45, 78, 89, 99, 99, 99, 123, 234, 465, 456]
    print(findLastVar(data, 8))  # 结果应该是 8
    print(findLastVar(data, 99))  # 结果应该是  15
