#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 19:09
# @Author  : sakura
# @Site    : 冒泡排序算法
# @File    : bubblesort.py
# @Software: PyCharm


"""冒泡排序
  优化： 因为正常的冒泡，需要对比‘后面’之前的所有数据。 所以我们在没有数据交换时候，就可以停止程序了

  空间复杂度O(1): 冒泡排序是原地排序算法
  相同元素没有交换过位置： 冒泡排序是稳定排序
  时间复杂度：
        最好情况  1 2 3 4 5 6 一次冒泡： 时间复杂度O(n)
        最坏情况  6 5 4 3 2 1 6 次冒泡： 时间复杂度O(n*n)
        平均情况  需要(n*(n-1)/2)/2 次交换，比较操作肯定要比交换操作多，而复杂度的上限是O(n*n)，所以平均情况时间复杂度
                  就是O(n*n)
        """


def bubble_sort(seq):
    """冒泡排序，数据按照从小到大的顺序排列
        seq： type:list"""
    length = len(seq)
    if length <= 1:
        return

    for j in range(length):
        flag = False  # 表示没有数据进行交换，此时可以退出程序
        # print(f"这是第{j + 1}次冒泡")
        # for i in range(length-1): # 末尾的元素已经是排序好的了
        for i in range(length - j - 1):
            if seq[i] > seq[i + 1]:
                # print(f"交换了{seq[i]}和{seq[i + 1]}")
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                flag = True  # 表示这次有数据交换
            # print(seq)
        if not flag:
            # print("结束冒泡排序")
            return


if __name__ == '__main__':
    seq = [4, 5, 6, 3, 2, 1]
    seq2 = [3, 5, 4, 1, 2, 6]
    bubble_sort(seq=seq)
    bubble_sort(seq=seq2)
