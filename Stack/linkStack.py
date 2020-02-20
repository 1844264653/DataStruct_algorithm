#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/25 12:04
# @Author  : sakura
# @Site    : 
# @File    : linkStack.py
# @Software: PyCharm

"""
链表实现栈：  采用带头节点【哨兵】的链表实现栈

        适用灵活方便，只有在需要的时候才会申请空间

        除了要存储元素外，还要额外的存储空间存储指针信息

"""


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class MyStack:
    def __init__(self):
        self.data = None
        self.next = None

    # 判断stack是否为空，空则返回true 否则返回false
    def isEmpty(self):
        if not self.next:
            return True
        return False

    # 获取栈的元素个数
    def size(self):
        size = 0
        head = self.next
        while head:
            head = head.next
            size += 1
        return size

    # 压栈
    def push(self, item):
        p = Node(x=item)
        p.next = self.next
        self.next = p

    # 弹栈
    def pop(self):
        tmp = self.next
        if tmp:
            self.next = tmp.next
            return tmp.data
        print("栈为空")

    # 栈顶元素
    def top(self):
        if self.next:
            return self.next.data
        print("栈为空")
