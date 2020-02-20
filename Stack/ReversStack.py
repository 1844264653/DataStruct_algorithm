#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 11:17
# @Author  : sakura
# @Site    : 
# @File    : ReversStack.py
# @Software: PyCharm

"""
***********************************反转栈中所有的元素***********************************

栈中    5  4  3  2  1   ————————>>  1  2  3  4  5


方法1：  申请一个额外的队列，依次入列，然后顺序出列入栈即可： 缺点： 需要额外的存储空间，空间复杂度比较高

方法2：  采用空间复杂度比较低的场景： 递归
            ———— 注意递归的终止条件和递归的定义
         对于  1  2  3  4  5  ：首先把栈底元素移动到栈顶得到  5  1  2  3  4
                                然后对不包含栈顶元素的子栈进行递归调用——对子栈元素进行反转：4  3  2  1
                                ......

        此外，由于栈的后进先出的特点，使得只能取得栈顶元素，因此要把栈底元素移动到栈顶也需要递归完成
        主要思路为： 把不包含该栈顶元素的子栈的栈底元素移动到子栈的栈顶，然后把栈顶的元素和子站的栈顶元素——其实就是与栈顶相邻的元素，
        进行交换

        为了更好理解递归调用，可以认为进行递归调用的时候，子栈已经把栈底元素移动到了栈顶
        e.g.  为了把  1  2  3  4  5 的栈底元素 5  移动到栈顶，首先对 2  3  4  5 进行递归调用得到  5  2  3  4
              然后对子栈顶元素  5 ，与栈顶元素  1  进行交换得到  5  1  2  3  4，实现了把栈底元素移动到栈顶

              ——————  实现递归代码的思路

"""


class MyStack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        """
        :return: top items
        """
        if not self.isEmpty():
            return self.items[self.size() - 1]
        return None

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def push(self, item):
        self.items.append(item)

    '''递归实现反转功能'''

    def exchange(self):  # 交换元素递归思想  ————  算法时间复杂度  N
        """递归的把栈底元素搞到栈顶来"""
        if self.isEmpty():
            print("栈已经被空了，不用再进行交换了")
            return
            # 假设此实就剩下最后两  陀  没有进行交换了
        top1 = self.peek()
        self.pop()
        if self.isEmpty():  # 刚好剩下一个元素  直接压栈就行
            self.push(top1)
        else:  # 1个以上
            self.exchange()  # 递归的交换  假设交换好了剩下的 ：  5  2  3  4  接下来把1 和 5 进行交换就行了
            top2 = self.peek()  # 5
            self.pop()  # 2 3 4
            self.push(top1)  # 1 2 3 4
            self.push(top2)

    def reverse(self):  # 最外层递归思想   算法时间复杂度  N*N
        if self.isEmpty():
            print("栈已经为空！")
            return
        # 将栈底元素移动到栈顶
        self.exchange()  # 假设第一次执行结果：5  1  2  3  4     ————算法时间复杂度  N
        top = self.peek()  # 栈顶元素  5
        self.pop()  # items  1  2  3  4
        self.reverse()  # 递归反转子栈  # 假设 1 2 3 4 反转好了 ——>   4 3 2 1  ————算法时间复杂度  N
        # 讲一开始的栈顶元素 top 放到栈顶就好了
        self.push(top)

    def isPopserial(self, pushserial, popserial):
        """根据入栈序列判断可能的出栈序列
                1.把push序列依次入栈，直到栈顶元素等于pop序列的第一个元素，然乎栈顶元素出栈，pop序列移动到第二个元素
                2.如果栈顶元素继续等于pop序列现在的元素，则继续出栈并pop后移；否则对push序列继续入栈
                3.如果push序列已经全部入栈，但是pop序列未全部遍历，而且栈顶元素不等于当前pop元素，那么这个序列不是一个
                    可能的出栈序列。如果栈为空，而且pop序列也全部被遍历过，则说明这是一个可能的pop序列。
            算法性能分析：这种方法在处理一个合理的pop序列的时候需要操作的次数最多，即把push序列进行一次压栈和出栈操作
                          操作次数为2N——所以时间复杂度为O(n),这种方法使用了额外的栈空间，空间复杂度为O(n)
        """
        if not pushserial or not popserial:  # 如果入栈序列和出栈序列为空，结束
            return False

        push_length = len(pushserial)
        pop_length = len(popserial)
        if push_length != pop_length:  # 保证两个序列的数据的一致性   我觉得这里真的可以放在开头
            return False
        pushIndex = 0
        popIndex = 0
        while pushIndex < push_length:  # 从入栈序列开始进行压栈，并且进行比较， 直到栈顶元素等于pop序列第一个元素
            self.push(item=pushserial[pushIndex])
            pushIndex += 1
            # 进行比较， 直到栈顶元素等于pop序列第一个元素
            while not self.isEmpty() and self.peek() == popserial(popIndex):
                self.pop()
                popIndex += 1
        # 栈为空， 且pop序列中的元素都被遍历完了
        return self.isEmpty() and popIndex == pop_length


if __name__ == '__main__':
    st = MyStack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.push(5)
    print(f"mystack is {st.items}")
    st.reverse()
    print(f"mystack is {st.items}")
