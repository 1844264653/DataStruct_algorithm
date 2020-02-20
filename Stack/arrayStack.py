#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/25 11:43
# @Author  : sakura
# @Site    : 
# @File    : arrayStack.py
# @Software: PyCharm

"""
数组实现 ： 压栈、弹栈、取栈顶元素、判断栈是否为空、以及获取栈中元素个数


    采用数组实现： 栈的空间是连续的， 一个元素占用一个存储空间

                   初始化申请的空间如果太大，造成空间的浪费
                   初始化申请的空间如果太小，后期需要经常扩充存储空间，扩容是个费时的操作，容易造成性能下降
"""


class MyStack:

    def __init__(self):
        self.items = []

    # 判断栈是否为空
    def isEmpty(self):
        return len(self.items) == 0

    # 栈空间大小
    def size(self):
        return len(self.items)

    # 栈顶元数
    def top(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        print("栈为空")

    # 弹栈
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        print("栈为空")

    # 压栈
    def push(self, item):
        self.items.append(item)
