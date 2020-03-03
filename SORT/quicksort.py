#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 18:24
# @Author  : sakura
# @Site    : 快速排序算法
# @File    : quicksort.py
# @Software: PyCharm

"""快速排序

     不是稳定排序
     可以是原地排序————需要通过巧妙设计
     时间复杂度O(nlogn)


     整体利用了分治的思想：取数据中任意值，比该数据小的放左边，比该数据大的放右边
                            递归的进行下去， 最终所有数据都有序
        思路实现1： 非原地排序， 空间复杂度为O(n)
                    申请两个数组，一个放比参考点小的，一个放比参考点大的，最后顺序拷贝到原数组即可
            ————  如果想优化空间复杂度，使之变成原地排序算法，，就不能申请太多的额外空间——再原地完成分区操作

        优化
        思想思路二： 原地排序 ———— 在原地完成分区操作即可
"""


def quicksort(l, left, right):
    """找到一个下标和元素，比它小地放左边，大的放右边  递归进行，直到只有一个元素"""
    if left <= right:
        # 获取到基准元素下标
        position = partition(l, left, right)
        # 左边递归
        quicksort(l, left, position - 1)
        # 右边
        quicksort(l, position + 1, right)


# def partition(l, left, right):  # 从大到小排
#     # 基准元素
#     x = l[right]  # 这里使用数组的最尾端元素
#     index = left  # 基准元素前面的元素做交换
#     for i in range(left, right):
#         # print(f"i,index:{i},{index}")
#         if l[i] > x:
#             l[index], l[i] = l[i], l[index]
#             index += 1
#         # print(l)
#     l[index], l[right] = l[right], l[index]
#     # print(l)
#     return index


def partition(l, left, right):  # 从小到大排序
    # 基准元素
    x = l[right]  # 这里使用数组的最尾端元素
    index = left  # 基准元素前面的元素做交换
    for i in range(left, right):
        # print(f"i,index:{i},{index}")
        if l[i] <= x:
            l[index], l[i] = l[i], l[index]
            index += 1
        # print(l)
    l[index], l[right] = l[right], l[index]
    # print(l)
    return index


"""
实践题：  在O(n)时间复杂下，找到无序数组中第K大元素  比如：[4,2,5,12,3] 第三大元素就是4

思路，对该数据进行分区：如果 选中的基准元素的下标p  刚好满足 p+1=k  那就arr[p]就是你想要的元素
                        如果 p+1>k  就在左边，则继续分区直到满足条件
                        如果 p+1<k，就在右边，则继续分区直到满足条件
                        
"""


def solution(arr, left, right, k):
    if left >= right:
        print(f"第{k}大元素为{arr[left]}")
    index = partition(arr, left, right)
    if index + 1 == k:
        # 此时刚好
        print(f"第{k}大元素为{arr[index]}")
        return
    if k > index + 1:  # 在右边
        solution(arr, index + 1, right, k)

    elif k < index + 1:  # 在左边
        solution(arr, left, index - 1, k)


def find_top_k(arr, k):
    """传入一个数组，在O(n)时间复杂度的情况下，查找出第K大的元素"""
    # 中止条件  p + 1 = k
    return solution(arr, 0, len(arr) - 1, k)


if __name__ == '__main__':
    l = [8, 10, 2, 3, 6, 1, 5]
    quicksort(l, 0, len(l) - 1)
    print(l)
    # for i in range(1, 6):
    #     find_top_k(arr=l, k=i)
