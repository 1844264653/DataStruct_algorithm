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
        counts[num] += 1  # 把相同的数丢一个桶里
    counts = list(itertools.accumulate(counts))  # 返回一系列的累加和 s = [1 2 3 4]  itertools.accumulate(s) >>[1, 3, 6, 10]

    # 临时数组，储存排序之后的结果
    a_sorted = [0] * len(a)
    for num in reversed(a):  # 这样可以保证排序算法是稳定的
        index = counts[num] - 1
        a_sorted[index] = num  # 放入对应的位置
        counts[num] -= 1  # 始终维持比该数要小的元素个数， num已经入队，所以少了一个

    a[:] = a_sorted


"""给你两个数组，arr1 和 arr2，

arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。
未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]
 

提示：

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
arr2 中的元素 arr2[i] 各不相同
arr2 中的每个元素 arr2[i] 都出现在 arr1 中
"""


class Solution:
    def relativeSortArray(self, arr1, arr2):
        # 其实就是一个桶排序  或计数排序？
        # 浓缩版
        # return sorted(arr1, key=(arr2 + sorted(set(arr1) - set(arr2))).index)
        # arr2 += sorted(set(arr1)-set(arr2)) # set(arr1) - set(arr2) # 表示arr1和arr2中不同的部分，差集
        # arr1.sort(key=arr2.index)
        # return arr1

        arr = [0 for _ in range(1001)]  # 由于题目说arr1的范围在0-1000，所以生成一个1001大小的数组用来存放每个数出现的次数。
        ans = []  # 储存答案的数组。
        for i in range(len(arr1)):  # 遍历arr1，把整个arr1的数的出现次数储存在arr上，arr的下标对应arr1的值，arr的值对应arr1中值出现的次数。
            arr[arr1[i]] += 1  # 如果遇到了这个数，就把和它值一样的下标位置上+1，表示这个数在这个下标i上出现了1次。
        for i in range(len(arr2)):  # 遍历arr2，现在开始要输出答案了。
            while arr[arr2[i]] > 0:  # 如果arr2的值在arr所对应的下标位置出现次数大于0，那么就说明arr中的这个位置存在值。
                ans.append(arr2[i])  # 如果存在值，那就把它加到ans中，因为要按arr2的顺序排序。
                arr[arr2[i]] -= 1  # 加进去了次数 -1 ，不然就死循环了。
        for i in range(len(arr)):  # 如果arr1的值不在arr2中，那么不能就这么结束了，因为题目说了如果不在，剩下的值按照升序排序。
            while arr[i] > 0:  # 同样也是找到大于0的下标，然后一直加到ans中，直到次数为0。
                ans.append(i)
                arr[i] -= 1
        return ans  # 返回最终答案。


def relat_sort(arr1, arr2):
    arr = [0] * (max(arr1) + 1)
    result = []
    for i in arr1:
        arr[i] += 1

    for per in arr2:
        while arr[per] > 0:
            result.append(per)
            arr[per] -= 1

    for s in arr1:
        while arr[s] > 0:
            result.append(s)
            arr[s] -= 1
    return result


if __name__ == '__main__':
    # a = [20, 5, 6, 77, 15, 16, 1, 15, 61, 15, 15, 21, 52, 63, 32, 55]
    # counting_sort(a)
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    s = Solution()
    # print(s.relativeSortArray(arr1, arr2))  # [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    print(relat_sort(arr1, arr2))
