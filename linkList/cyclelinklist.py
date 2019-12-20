#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 20:04
# @Author  : sakura
# @Site    : 
# @File    : cyclelinklist.py
# @Software: PyCharm


"""
1. 单链表
2. 循环链表  √
3. 双向链表
4. 双向循环链表
"""


class Node(object):

    def __init__(self, item=None):
        self.item = item
        self.next = None


class CycleLinkList(object):

    def __init__(self):
        self.head = Node(item="null")
        self.length = 0

    def traverse(self):
        cur = self.head.next
        if self.length == 0:
            print("链表不存在")
            return self.head
        print(f"当前值：{cur.item}")
        while cur.next != self.head.next:
            cur = cur.next
            print(f"当前值：{cur.item}")
        print(f"长度{self.length}")

    def add(self, index=0, item=None):
        index = self.length if index > self.length else index
        node = Node(item=item)
        cur = self.head
        pos = -1
        length = self.length
        while pos < length:
            if pos == index - 1:
                node.next = cur.next
                cur.next = node
                self.length += 1
            pos += 1
            cur = cur.next
            # if index != self.length:
            # 循环链表的特殊性在于末尾连接首部 , 为了不用每次都遍历到末尾，所以特殊处理，提升代码执行效率
            # break
        cur.next = self.head.next

        return cur

    def delete(self, item=None):  # 删除头节点比较特殊
        flag = 0
        cur = self.head
        if self.length == 1:
            self.head.next = Node
            self.length -= 1
            return self.head
        pos, length = 1, self.length
        while pos <= length:
            if cur.next.item == item:
                cur.next = cur.next.next
                flag = 1
            cur = cur.next
            pos += 1
        self.length = self.length - 1 if flag else self.length
        self.head.next = cur

        return cur

    def revert(self, head=None):
        """递归翻转, 需要将末尾连接也反向，导致递归无法终结"""

        # 处理断开尾节点，变成单链表比较好反转
        if not head or not head.next:
            print("链表不存在或者只有一个节点")
            return
        cur = head
        while cur.next.item != self.head.next.item:
            cur = cur.next
        old_head = cur.next
        cur.next = None  # 断开连接

        def _revert(head=None):
            if not head or not head.next:  # 递归的结束条件
                print("链表不存在或者只有一个节点")
                return head
            new_head = _revert(head.next)
            head.next.next = head
            head.next = None
            return new_head

        new_head = _revert(head=old_head)
        old_head.next = new_head  # 接上循环
        self.head.next = new_head


if __name__ == '__main__':
    cyclelink = CycleLinkList()
    cyclelink.add(index=0, item=1)
    cyclelink.add(index=1, item=2)
    # cyclelink.delete(item=2)
    # cyclelink.traverse()
    cyclelink.add(index=0, item=100)
    cyclelink.add(index=5, item=1000)
    # cyclelink.traverse()
    # cyclelink.delete(item=100)
    # cyclelink.delete(item=1000)
    # cyclelink.delete(item=541564)
    cyclelink.traverse()
    cyclelink.revert(cyclelink.head.next)
    cyclelink.traverse()
