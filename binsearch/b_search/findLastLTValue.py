#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 18:32
# @Author  : sakura
# @Site    : 
# @File    : findLastLTValue.py
# @Software: PyCharm

"""寻找最后一个小于等于给定值的元素
        e.g. [3,5,6,8,9,10]  最后一个小于7的元素就是6"""


def findLastLTVar(data, target):
    low, high = 0, len(data) - 1

    while low <= high:
        mid = low + (high - low >> 1)
        if data[mid] > target:
            high = mid - 1
        else:  # data[mid] <= target
            # 1.  如果mid是最后一个元素  ok
            #  2. 如果 data[mid+1] > target  ok
            if mid == len(data) - 1 or data[mid + 1] > target:
                return mid
            else:
                # 否则 最后一个比target大或者等于的数 肯定在后面的区间
                low = mid + 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 8, 8, 8, 8, 12, 45, 78, 89, 99, 99, 99, 123, 234, 465, 456]
    print(findLastLTVar(data, 8))  # 结果应该是 8
    print(findLastLTVar(data, 99))  # 结果应该是  15
    print(findLastLTVar(data, 7))  # 结果应该是 4
    print(findLastLTVar(data, 88))  # 结果应该是  11
