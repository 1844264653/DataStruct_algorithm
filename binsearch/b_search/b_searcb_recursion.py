#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 17:05
# @Author  : sakura
# @Site    : 递归式二分查找
# @File    : b_searcb_recursion.py
# @Software: PyCharm

"""利用递归来实现一个二分查找: 就是容易栈溢出"""


# 如果利用切片  就改动了原来的数据
# def bin_search(data, target):
#     # 递归停止跳出条件
#     low, high = 0, len(data) - 1
#     if low > high:
#         return -1
#     mid = low + (high - low) >> 1
#     if target == data[mid]:
#         print("ok")
#         return mid
#     elif target > data[mid]:
#         return bin_search(data[mid + 1: high], target)
#     else:
#         return bin_search(data[low: mid - 1], target)

def bin_search(data, target, high, low):
    if low > high:
        return -1
    mid = low + (high - low) >> 1
    if target == data[mid]:
        return mid
    elif target > data[mid]:
        return bin_search(data, target, high, mid + 1)
    else:
        return bin_search(data, target, mid - 1, low)


if __name__ == '__main__':
    import random

    data = [random.randint(0, 2 ** 4) for _ in range(2 ** 4)]
    # data = [1, 2, 5, 4, 8, 12, 45, 6, 453, 454, 354, 354, 34, 343, 543, 54]
    rand_int = data[2]
    data = sorted(list(set(data)))
    res = bin_search(data, target=rand_int, high=len(data) - 1, low=0)
    print(res)
