#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 20:53
# @Author  : sakura
# @Site    : 希尔排序算法
# @File    : shellsort.py
# @Software: PyCharm


"""希尔排序

希尔排序(Shell's Sort)是插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort），
是直接插入排序算法的一种更高效的改进版本。希尔排序是非稳定排序算法

      第一次增量的取法为： d=count/2;

      第二次增量的取法为:  d=(count/2)/2;

      最后一直到: d=1;

"""


def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)  # 步长

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)  # 调整步长

    print(arr)


# 加餐   装饰器


def w1(func):
    def inner():
        print('...验证权限...')
        func()
        print(func.__name__)  # 这里是函数本身的名字

    return inner


@w1
def f1():
    print('f1 called')


@w1
def f2():
    print('f2 called')


def say_hello(country):
    def wrapper(func):
        def deco(*args, **kwargs):
            print(args, kwargs)
            if country == 'china':
                print('你好！')
            elif country == 'america':
                print('hello')
            else:
                return
            func(*args, **kwargs)

        return deco

    return wrapper


@say_hello('china')
def chinese(name):
    print(name)
    print('我来自中国。')


@say_hello('america')
def america(name):
    print(name)
    print('I am from America.')


if __name__ == '__main__':
    arr = [49, 38, 65, 97, 76, 13, 27, 49, 55, 4]
    shellSort(arr)
    # f1()
    # print(f1.__name__)  # 这里是装饰器里  inner    函数名字被修改了
    # f2()

    # america(name="american")
    # print('-' * 20)
    # chinese(name="china")
