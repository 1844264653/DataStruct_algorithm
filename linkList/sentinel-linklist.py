#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/17 21:54
# @Author  : sakura
# @Site    : 
# @File    : sentinel-linklist.py
# @Software: PyCharm


"""
1. 单链表   √   可以利用哨兵优化  √
2. 循环链表
3. 双向链表
4. 双向循环链表
"""


class Node(object):

    def __init__(self, item=None):
        self.item = item
        self.next = None


class SingleList(object):
    """
    增加哨兵作为链表头
    假设链表不存在重复元素
    """

    def __init__(self):
        self.head = Node(item="null")
        self.length = 0

    # 遍历
    def traverse(self):
        """有哨兵链表头作为 ”head”"""
        cur = self.head
        while cur.next:
            print(f"当前值是：{cur.next.item} ")
            cur = cur.next
        print(f"长度是 {self.length}")

    # 插入   任意位置插入一个元素
    def add(self, index=0, item=None):
        index = self.length if index > self.length else index
        node = Node(item=item)
        cur = self.head
        pos = -1
        while True:
            if pos == index - 1:
                node.next = cur.next
                cur.next = node
                self.length += 1
                break
            pos += 1
            cur = cur.next

    # 删除   删除任意指定节点
    def delete(self, item):
        """删除值为item的节点  p.next = p.next.next"""
        cur = self.head
        while cur.next:
            if cur.next.item == item:
                cur.next = cur.next.next
                self.length -= 1
                return
            cur = cur.next
        print(f"不存在value:{item}节点")

    # 判断是否存在环
    def has_cycle(self, head):
        """判断是否存在环 True/False"""
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # 链表的中心节点  如果链表为空或者链表只有一个节点(head.next == None)，则无法进入循环，直接返回原链表。
    # 接下来，慢指针slow每次走一步，快指针fast每次走两步，直到循环结束，如果链表长度为奇数，此时slow节点就是中间节点；
    # 如果链表长度为偶数，中间节点应该有两个，这里返回的slow节点是中间两个节点的第一个，slow.next则为中间节点的第二个
    def middle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow if self.length % 2 else [slow, slow.next]

    def revert(self, head=None):
        """递归翻转"""

        def _revert(head=None):
            if not head or not head.next:  # 递归的结束条件
                print("链表不存在或者只有一个节点")
                return head
            new_head = _revert(head.next)
            head.next.next = head
            head.next = None
            return new_head

        self.head.next = _revert(head=head)


if __name__ == '__main__':
    sentinel = SingleList()
    for i in range(1):
        sentinel.add(index=i, item=i)
    sentinel.traverse()
    sentinel.revert(head=sentinel.head.next)
    sentinel.traverse()

