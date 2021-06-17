#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 21:10
# @Author  : sakura
# @Site    : 桶排序算法
# @File    : bucketsort.py
# @Software: PyCharm

"""桶排序算法

 核心思想是将要排的数据分导几个有序的桶里， 每个桶里的数据再单独进行排序——桶内部使用快速排序。
 桶内排序后，再把每个桶里的数据按照顺序依次取出，组成的序列就是有序的了


 时间复杂度： O(n)
 空间复杂度： O(n)  —— 不是原地排序算法
 不是稳定排序算法


 对数据的要求：
            1. 首先，要排序的数据需要很容易就能划分成 m 个桶，并且，桶与桶之间有着天然的大小顺序。
               这样每个桶内的数据都排序完之后，桶与桶之间的数据不需要再进行排序。
            2. 其次，数据在各个桶之间的分布是比较均匀的。如果数据经过桶的划分之后，有些桶里的数据非常多，有些非常少，
                很不平均，那桶内数据排序的时间复杂度就不是常量级了。
                在极端情况下，如果数据都被划分到一个桶里，那就退化为 O(nlogn) 的排序算法了。

适应场景：桶排序比较适合用在外部排序中。所谓的外部排序就是数据存储在外部磁盘中，
          数据量比较大，内存有限，无法将数据全部加载到内存中。"""

from SORT import quicksort


def bucketsort(obj_arr, bucketsize):
    """
    1. 桶的个数通常选择需要排序的数据的个数，或者是最大值-最小值+1， obj 可以是任何对象
    :return:
    """
    minValue, maxValue = obj_arr[0], obj_arr[1]

    for i in obj_arr:
        if i < minValue:
            minValue = i
        elif i > maxValue:
            maxValue = i

    # 桶数量
    bucketcount = (maxValue - minValue) + 1  # bucketsize
    # 对应的桶
    bucket_lists = list([] for _ in range(bucketcount))

    # 把数据放入相应的桶
    for i in obj_arr:
        bucket_index = (i - minValue) // bucketsize
        bucket_lists[bucket_index].append(i)

        # 桶内快排
    count = 0
    for per_bucket in bucket_lists:
        if not per_bucket:
            break
        # print(f"排序前{per_bucket}")
        quicksort.quicksort(per_bucket, 0, len(per_bucket) - 1)  # 注意  这里的快排是从大到小排序的
        # print(f"排序后{per_bucket}")
        count += 1
    print(count)

    # 合并数据
    result = []
    for j in bucket_lists:
        if len(j) != 0:
            result.extend(j)
    return result


if __name__ == '__main__':
    import random

    s = []
    for i in range(1, 200, 2):
        s.append(i)
    random.shuffle(s)
    print(s)
    arr = bucketsort(obj_arr=s, bucketsize=20)
    print(arr)
