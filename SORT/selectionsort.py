#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 20:30
# @Author  : sakura
# @Site    : 选择排序算法
# @File    : selectionsort.py
# @Software: PyCharm


"""选择排序

   和插入算法类似
   是从未排序区间中找到最小元素，将其放到已经排序的区间末尾

   空间复杂度O(1): 是原地排序算法
   最好，最坏、平均情况时间复杂度都是O(n*n)
   选择排序算法不是稳定排序算法"""


def selection_sort(seq):
    """seq: type:list"""
    length = len(seq)
    if length <= 1:
        return

    for i in range(length):
        min = seq[i]
        min_index = i
        for j in range(i, length):
            if seq[j] < min:
                min = seq[j]
                min_index = j
        seq[i], seq[min_index] = seq[min_index], seq[i]
        print(seq)

    print(seq)


if __name__ == '__main__':
    seq = [4, 5, 6, 3, 2, 1]
    selection_sort(seq)
