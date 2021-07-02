#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/16 19:58
# @Author  : sakura
# @Site    : 
# @File    : linklist.py
# @Software: PyCharm

"""
1. 单链表   √   可以利用哨兵优化
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
        """链表头存在与否 ， 链表尾指针域指向NULL"""
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
                node.next = current.next
                current.next = node
                self.length += 1
                return
            pos += 1
            current = current.next

    # 读    遍历的方法
    def traverse(self, head=None):
        if not head:
            print("the linklist is not exist or Null !")
            return
        current = head
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

    # 单链表反转
    # 方法1  ： 利用数组的索引，太浪费空间  略过
    # 方法2  :  利用三个指针遍历， 挨个节点进行连接
    # 方法3  ： 利用插入排序法的思想去搞， 这个方法挺好的, 将2-N个依次倒叙
    # 方法4  ： 链表就是一颗只有一颗叉的树，对于树的问题思想，我们可以用递归进行实现，更加具有面向对象的思想
    def invert_1(self, head):
        """浪费空间，省略"""
        pass

    def invert_2(self, head):
        """利用三指针的方法，逐个连接就好"""
        if not head or not head.next:  # 递归的结束条件
            print("链表不存在或者只有一个节点")
            self.head = head
            return head
        p = head
        q = head.next
        head.next = None  # 头变成尾巴   指向空 1 -> none
        while q:
            r = q.next  # 指向第三位置【有点像保留数据】p(1) -> 2(q) -> 3(r) -> 4 -> 5
            q.next = p  # p(1) <- 2(q)  3(r) -> 4 -> 5
            p, q = q, r
        head = p
        self.head = head
        return self.head

    def invert_3(self, head):
        """插入排序法思想"""
        if not head or not head.next:  # 递归的结束条件
            print("链表不存在或者只有一个节点")
            self.head = head
            return head
        cursor = head.next
        while cursor.next:
            # 一： 1 - 2 - 3 - 4 - 5    准备交换 2  3 位置  依次类推
            q = cursor.next  # 标记 3
            cursor.next = q.next  # 1 - 2 - 4 - 5   3 - 4 - 5
            q.next = head.next  # 3 - 2 - 4 - 5   1 - 2 - 4 - 5
            head.next = q
        cursor.next = head  # 一定要先成环，不能先断开head
        head = cursor.next.next  # 新头变成了 5
        # 断环
        cursor.next.next = None
        self.head = head
        return self.head

    def invert_4(self, head):
        """递归思想 : 倒序思考   e.g.   A - > B -> C -> D
           最终结果    ：  D -> C -> B -> A
           倒数第一步  ：  D -> C -> B    A    当成两个整体对象，  ↑ 连接两个整体
           倒数第二步  ：  D -> C    B    A    ****************。  ↑ 连接两个整体
           倒数第三步  ：  D    C    B    A
           ........
            """
        if not head or not head.next:  # 递归的结束条件
            print("链表不存在或者只有一个节点")
            self.head = head
            return head
        new_head = self.invert_4(head.next)
        head.next.next = head
        head.next = None
        return new_head


if __name__ == '__main__':
    singlelist = SingleLinkList()
    singlelist.append(1)
    singlelist.append(2)
    singlelist.append(3)
    singlelist.append(4)
    singlelist.append(5)
    singlelist.traverse(head=singlelist.head)
    new = singlelist.invert_4(head=singlelist.head)  # ok
    singlelist.traverse(head=singlelist.head)
