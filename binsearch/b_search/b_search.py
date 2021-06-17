#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/29 16:09
# @Author  : sakura
# @Site    : 二分查找
# @File    : b_search.py
# @Software: PyCharm

import wget

"""二分查找
       二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想，
       每次都通过跟区间的中间元素对比，讲待查找元素的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为零

       O(logn)  惊人的查找速度

       二分查找是一种及其高效的时间复杂度的查找算法，
       有的时候甚至比时间复杂度是常量级别的O（1）的算法更加高效
                对于常量的复杂度，O（1）有可能表示的是一个非常大的常量值， 比如  1000  1000000
                但是即便n非常大，logn也非常小，例如2的32次方 大约是42亿了，也就是说我们再42亿个数据中用二分法查找一个数据，
                最多需要比较32次



        二分查找 更加适合用在 ‘近似’查找问题， 在这类问题上， 二分查找的优势更加明显

        等值查询等 更倾向于用散列表或者二叉查找树  即使没有二分查找更省内存，但是内存如此紧缺的情况确实不多
"""


# 循环实现

def b_search(data: list, target: int) -> int:
    max_num = len(data) - 1
    min_num = 0
    times = 0
    while min_num <= max_num:  # 注意点 1
        times += 1
        mid = min_num + (max_num - min_num >> 1)  # 这里要注意  不同语言的位运算优先级不一样  python加减法优先位运算
        if data[mid] == target:
            print(times)
            return mid
        elif target > data[mid]:
            min_num = mid + 1
        else:
            max_num = mid - 1
    print(times, "没有结果")
    return -1


if __name__ == '__main__':
    import random

    data = [random.randint(0, 2**25) for _ in range(2**25)]
    rand_int = data[60]
    data = sorted(list(set(data)))
    res = b_search(data, target=rand_int)
    print(res)
