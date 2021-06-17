#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 16:59
# @Author  : sakura
# @Site    : 归并排序算法的哨兵优化
# @File    : mergesort_improve.py
# @Software: PyCharm

"""哨兵优化归并算法"""


def sort(l):
    """每个序列进行排序"""
    if len(l) <= 1:
        return l
    mid = len(l) // 2  # 从中点进行拆分数组
    left = sort(l[:mid])
    right = sort(l[mid:])
    # return merge(l[:mid], l[mid:])
    return merge(left, right)


def merge(left, right):
    """利用哨兵进行简化代码， 只需要在左右两个部分增加一个同样的哨兵最大值， 那么末尾就不会再有多余的item需要进行追加"""
    i = j = 0
    tmp = []
    max_sentinel = 99999  # 事实上对应业务中呢？ 如何判断最大值呢？
    left.append(max_sentinel)
    right.append(max_sentinel)
    while left[i] != max_sentinel:
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    return tmp


if __name__ == '__main__':
    l = [1, 5, 6, 2, 3, 4, 0, 11, 50]
    print(sort(l))
