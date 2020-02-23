#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 16:14
# @Author  : sakura
# @Site    : 归并算法
# @File    : mergesort.py
# @Software: PyCharm


"""归并排序
        是稳定的排序算法
        时间复杂度为O(nlogn) ---归并排序不关心数组的初始状态
        不是原地排序算法——在合并的时候，需要借助额外的储存空间—— 空间复杂度为O(n)


        使用哨兵优化性能
在上述 merge 函数中有三处使用了 while 循环，第一个 while 循环条件中还有两个范围判断语句，当数据量非常大时，这些过多的判断势必会影响算法的性能。

我们知道，在编程中可以借助哨兵来简单条件判断，从而可以写出 bug 更少的代码，进而优化性能。

上述中的 merge 函数主要目的主是合并两个有序数组，但是为了在比较的过程中防止越界，加入了 i < r 和 j < q 来防止左右部分越界，最后防止某部分有剩余元素从而多写了两个 while 循环。

其实在大多数情况下，越界的情况是非常少的，那么每一次循环对越界的检查也会浪费 CPU 资源，而哨兵就是优化条件判断的。

思考：
1、如果左右部分的最后一个元素都是最大且相等，那么当左边的元素循环结束时，右边也必定结束，这样只用一个 while 就可以搞定，而且只需要一个 i < r 就够了，节省一个条件判断。

2、范围比较 i < r 需要 cpu 对每个二进制位进行比较，如果换成不等于判断，只要一个二进制位不同，就可以得出结果，理论上也可以更快些。


分别在左部分和右部分的最后加入最大值的哨兵，可以减化 merge 函数的编码，使用哨兵有以下三点优化：

1、减少了 while 的个数，简化了编码过程
2、减少了 while 循环的条件判断
3、将范围判断改为不等于判断

"""


def merge(left, right):
    """
    :param left:序列左半部分
    :param right: 序列又半部分
    :return: 返回合并后的序列
    """
    # 两个坐标作为两个拆分序列的下标
    i = j = 0
    # 需要一个临时的空间来存放merge后的数据 —— 递归中，因为每次只有一个函数在执行，所以空间复杂度为O(n)
    tmp = []
    #  两个数组进行同步位移合并
    print(left, right)
    while i < len(left) and j < len(right):  # 当左右两个数组有一个移动到末尾，比较结束，剩下的，直接追加即可
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    # 如果left先跑完  则把右边的追加到临时空间
    tmp.extend(right[j:]) if i == len(left) else tmp.extend(left[i:])
    return tmp


def sort(l):
    """每个序列进行排序"""
    if len(l) <= 1:
        return l
    mid = len(l) // 2  # 从中点进行拆分数组
    left = sort(l[:mid])
    right = sort(l[mid:])
    return merge(left, right)


if __name__ == '__main__':
    l = [1, 5, 6, 2, 3, 4]
    print(sort(l))  # [1, 2, 3, 4, 5, 6]
    # s = [1, 5, 6, 2, 3]
    # print(sort(s))
