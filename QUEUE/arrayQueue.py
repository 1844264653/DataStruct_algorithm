#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 14:19
# @Author  : sakura
# @Site    : 
# @File    : arrayQueue.py
# @Software: PyCharm

"""
数组实现队列：
    出列后数组的前半部分的空间不能充分被利用
        解决这个问题的方法为  把数组看成一个环形的空间——循环队列，当数组最后一个位置被占用后，可以从数组首位置开始循环利用
"""


class MyQueue:
    def __init__(self):
        self.arr = []
        self.front = 0  # 对头指针——下标
        self.rear = 0  # 队尾指针——下标

    # 队列是否为空
    def isEmpty(self):
        # return len(self.arr) == 0
        return self.front == self.rear

    # 队列大小
    def size(self):
        # return len(self.arr)
        return self.rear - self.front

    # 队尾元素
    def getBack(self):
        if not self.isEmpty():
            return self.arr[self.rear - 1]
        print("队列为空！")

    # 队首元素
    def getFront(self):
        if not self.isEmpty():
            return self.arr[self.front]
        print("队列为空！！")

    # 出列【队首】
    # def deQueue(self):   这样实现其实不是很正确，作为优化我们可以只移动指针就行，而元素先不删除，需要时一起批量删除！！
    #     if self.rear > self.front:
    #         top_item = self.arr[self.front]
    #         self.arr.pop(self.front)
    #         return top_item
    #     print("队列为空")

    # 出列【队首】
    def deQueue(self):
        if self.rear > self.front:
            self.front += 1
            return
        print("队列为空")

    # 入列  【队尾】
    def enQueue(self, item):
        self.arr.append(item)
        self.rear += 1
