#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 18:21
# @Author  : sakura
# @Site    : 
# @File    : findFirstGTValue.py
# @Software: PyCharm

"""查找第一个大于等于给定值的元素
  e.g.  [3,4,6,7,10]  如果查找第一个大于等于5的元素， 那就是6"""


def findFirstGTvalue(data, target):
    low, high = 0, len(data) - 1

    while low <= high:
        mid = low + (high - low >> 1)
        if data[mid] < target:  # 如果找到的元素比target小 那么应该在更大的区间找
            low = mid + 1
        else:  # target <= data[mid]
            # 1. 如果是data[0]   那千前面没有比target大的元素了 ok
            #    如果 data[mid - 1] < target  ok
            if mid == 0 or data[mid - 1] < target:
                return mid
            else:  # 否则 前面还有大于等于target的数  应该在前面的区间继续寻找
                high = mid - 1


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 8, 8, 8, 8, 12, 45, 78, 89, 99, 99, 99, 123, 234, 465, 456]
    print(findFirstGTvalue(data, 7))  # 结果应该是 5
    print(findFirstGTvalue(data, 99))  # 结果应该是  13
