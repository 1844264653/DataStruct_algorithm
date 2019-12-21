#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/21 20:17
# @Author  : sakura
# @Site    : 
# @File    : LRU.py
# @Software: PyCharm

"""
利用链表实现LRU淘汰缓存池算法：
    维护一个有序的单链表，越靠近链表尾部的节点是越早之前访问的。
    当有一个新的数据被访问时，我们从链表头部开始顺序遍历链表：
    1. 如果该数据之前被缓存在链表中了，我们遍历得到这个数据对应的节点，并将器从原来的位置删除，然后再插入到链表的头部
    [为什么要删除呢？ 因为要保持数据的有序性——时间有序]!!!!!
    2. 如果此数据没有在缓存链表中，又可以分为两种情况：
                    1. 如果此时缓存未满，则将此节点直接插入到链表头部；
                    2. 如果此时缓存已满，则链表尾节点删除，将新的数据节点插入链表头部
    不管缓存是否存满，，都需要遍历一遍链表，所以基于链表的实现思路，缓存访问时间复杂度是O(n)

    实际上我们可以继续优化这个思路，比如引入   散列表 来记录每个数据的位置，将缓存的访问复杂度下降到O(1)

    ps：
        1.可以利用  collections.OrderedDict  的底层实现【循环双端链表】去实现一个LRU算法
        2.functools.lru_cache  是已经实现好的一个LRU算法，也是利用双端链表+字典实现的
"""

import time, functools


# 经典的斐波那契数列
@functools.lru_cache(maxsize=3)
def fibonacci(n=None):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start = time.time()
    print(fibonacci(300))  # 在不使用缓存的时候，计算机一直在响，且没有出现计算结果
    end = time.time()
    print(end - start)  # 4.005139350891113
    # 当加上缓存之后  输入300层  只用了  0.000993490219116211    NB
