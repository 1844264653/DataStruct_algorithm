#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 14:41
# @Author  : sakura
# @Site    : 
# @File    : linkQueue.py
# @Software: PyCharm

"""
链表实现：  比其数组实现，链表实现具有更好的灵活性
            多了用来存储节点关系的指针空间

            如果用循环链表来实现，就只需要一个指向最后元素的指针即可
            因为通过指向链表尾元素可以非常容易找到链表的首节点
"""


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class MyQueue:
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    # 是否为空
    def isEmpty(self):
        return self.pHead is None

    # 队列大小
    def size(self):
        size = 0
        p = self.pHead
        while p:
            p = p.next
            size += 1
        return size

    # 队首元素
    def getFront(self):
        return self.pHead.data if self.pHead else None

    # 队尾元素
    def getBack(self):
        return self.pEnd.data if self.pEnd else None

    # 入列
    def enQueue(self, item):
        node = Node(x=item)
        if self.isEmpty():
            self.pHead = self.pEnd = node
            return
        self.pEnd.next = node
        self.pEnd = node

    # 出列
    def deQueue(self):
        if self.isEmpty():
            print("队列为空， 出列失败")
            return False
        self.pHead = self.pHead.next
        if self.isEmpty(): # 这里要注意下一个元素的情况下出列
            self.pEnd=self.pHead = None
