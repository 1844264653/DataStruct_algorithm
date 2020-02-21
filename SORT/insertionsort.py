#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 20:00
# @Author  : sakura
# @Site    : 插入排序算法
# @File    : insertionsort.py
# @Software: PyCharm


"""插入排序

    将数组中的数据分为两个区间，已排序区间和未排序区间
    初始已排序区间只有一个元素，就是数组的第一个元素
    插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的位置将其插入
    并保证已排序区间数据一直有序。重复这个过程，直到未排序区间中元素为空


    过程中不需要额外的存储空间，所以是空间复杂度为O(1)：是原地排序算法
    是稳定的排序算法
    时间复杂度是  O(N*N)

    -----优化思路： 希尔排序
    """


def insertion_sort(seq):
    """
    :param seq： type:list
    """
    length = len(seq)
    if length <= 1:
        return

    for i in range(1, length):
        j = i - 1
        while j >= 0:
            if seq[j + 1] < seq[j]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                print(seq)
            j -= 1

    print(seq)


if __name__ == '__main__':
    seq = [4, 5, 6, 1, 3, 2]
    insertion_sort(seq)
