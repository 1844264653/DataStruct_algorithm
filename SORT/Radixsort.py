#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 23:22
# @Author  : sakura
# @Site    : 基数排序
# @File    : Radixsort.py
# @Software: PyCharm


"""基数排序算法

时间复杂度O(n)
空间复杂度O(n)——不是原地排序算法
是稳定性算法

基本思想：将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。
            然后，从最低位开始，依次进行一次排序。
            这样从最低位排序一直到最高位排序完成以后,数列就变成一个有序序列。


            其实就是多次基于桶排序，  如果是数字就10 个桶
            数字的话 只能从低位开始排起， 反过来的话 数据依然还是无序的

        基数排序法对数据的要求还是比较严格的，需要可以分割出独立的‘位’来比较，
        而且位之间有递进的关系，如果a数据的高位比b数据大，剩下的就不用比较了。
        除此之外，每一位的数据范围不能太大，要可以用线性排序算法来排序，
        否则，基数排序的时间复杂度就无法做到O（n）

"""


def radix_sort(s):
    """基数排序"""
    i = 0  # 记录当前正在排拿一位，最低位为1
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list = [[] for _ in range(10)]  # 初始化桶数组 因为用数字举例  所以10 个桶
        for x in s:
            bucket_list[int(x / (10 ** i)) % 10].append(x)  # 找到位置放入桶数组
        print(bucket_list)
        s.clear()
        for x in bucket_list:  # 放回原序列
            for y in x:
                s.append(y)
        i += 1


if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    radix_sort(a)
    print(a)
