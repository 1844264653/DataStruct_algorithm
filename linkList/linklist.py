#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 19:58
# @Author  : sakura
# @Site    : 
# @File    : linklist.py
# @Software: PyCharm

"""
1. 单链表
2. 循环链表
3. 双向链表
4. 双向循环链表
"""


#  单链表 ： 在内存中不需要一块连续的内存空间，它通过 指针 将一组内存块串联起来使用
#  结构 ： 结点 （数据块 + 后续指针next）-- 数据域和指针域
#  实现思路： 实现一个节点， 多个节点对象组成一个单链表对象
#  场景： 增 + 删 + 遍历（读）+ 改   其中改可以直接赋值


class Node(object):
    """
    一个节点对象： 节点数据块 + 下一个节点的存储位置
    """

    def __init__(self, item=None):
        self.item = item
        self.next = None


class SingleLinkList(object):

    # 考虑链表是否存在
    def __init__(self):
        """链表头存在与否 ， 链表尾指针域只想NULL"""
        self.head = None
        self.length = 0

    # 增  追加   直接在链表末尾追加一个元素--node即可， ps： 默认追加
    def append(self, item):
        node = Node(item=item)
        if not self.head:  # 如果链表不存在，直接作为第一个节点
            self.head = node
            self.length += 1
            print("链表不存在， 我是头了现在", self.head.item)
            return item
        # 否则找到末尾，追加到链表末尾
        current = self.head
        while current.next:
            current = current.next
        # 否则 末尾节点指针域指向NULL时候，追加数据，并且next指向NULL
        current.next = node
        self.length += 1

    # 增  压栈
    def pull(self, item=None):
        node = Node(item=item)
        if not self.head:  # 如果链表不存在，直接作为第一个节点
            self.head = node
            self.length += 1
            print("链表不存在， 我是头了现在", self.head.item)
            return item
        # 否则将该node作为链表头
        self.head, node.next = node, self.head
        self.length += 1

    # 增  在指定位置插入
    def insert(self, index=None, item=None):
        """
        将index-1 节点指向 index节点，将index节点指向index +1 节点
        """
        if index > self.length:
            raise ValueError(f"the index out of range,the linklist`s most length :{self.length}")
        if index == 0:
            self.pull(item=item)
            return
        if index == self.length:
            self.append(item)
            return
            # 插入
        current = self.head
        node = Node(item=item)
        pos = 0
        while True:
            if pos == index - 1:
                current.next = node
                node.nex = current.next.next
                self.length += 1
                return
            pos += 1
            current = current.next

    # 读    遍历的方法
    def list(self):
        if not self.head:
            print("the linklist is not exist or Null !")
            return
        current = self.head
        while current.next:
            print("the current value is %s" % current.item)
            current = current.next
        print("the final item is %s" % current.item)

    # 删    delete的方法， 删除链表中数据等于item
    def delitem(self, item):
        """这个item是否存在， 存在删除--指针指向下下个节点， 遍历完不存在则返回
           尝试： 该节点的下一个节点的值等于item  会更好处理一点
        """
        flag = 0  # 判断删除了几次
        current = self.head
        while current.next:
            if current.next.item == item:  # 这里直接比较下一个节点的值，更好处理
                print(f"删除{item}")
                flag += 1
                current.next = current.next.next
                continue
            current = current.next
        else:  # 处理只有一个节点的情况
            if current.item == item:
                flag += 1
                print(f"只有一个节点，且恰好是这个节点，链表删除完了, 删除{item}")
                self.head = None
            self.length -= flag
            print(flag)
            if not flag:
                print("该数据不存在链表中")


if __name__ == '__main__':
    singlelist = SingleLinkList()

