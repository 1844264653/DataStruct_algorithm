#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 22:56
# @Author  : sakura
# @Site    : 计数排序
# @File    : countsort.py
# @Software: PyCharm

"""计数排序算法
时间复杂度：O(n)
空间复杂度：  根据所排序最大值确定
不是原地排序算法

核心思想：当要排n个数据时候，并且数据范围并不大！！！，比如最大值为K，我们就可以把数据分成K个桶，每个桶内的数值都是相同的
          节省了桶内排序的时间


        计数的过程思想非常巧妙，需要查看资料记忆！！https://time.geekbang.org/column/article/42038

        计数排序是桶排序的一种特殊情况 可以把计数排序当成每个桶里只有一个元素的情况，它是一个非基于比较的排序算法，
        它的优势在于在对一定范围内的整数排序时，它的复杂度为Ο(n+k)（其中k是整数的范围），快于任何比较排序算法。"""
import itertools


# from typing import List


def counting_sort(a):
    if len(a) <= 1:
        return

    # a中有counts[i]个数不大于i
    counts = [0] * (max(a) + 1)
    for num in a:
        counts[num] += 1
    counts = list(itertools.accumulate(counts))  # 返回一系列的累加和 s = [1 2 3 4]  itertools.accumulate(s) >>[1, 3, 6, 10]

    # 临时数组，储存排序之后的结果
    a_sorted = [0] * len(a)
    for num in reversed(a):  # 这样可以保证排序算法是稳定的
        index = counts[num] - 1
        a_sorted[index] = num  # 放入对应的位置
        counts[num] -= 1  # 始终维持比该数要小的元素个数， num已经入队，所以少了一个

    a[:] = a_sorted


