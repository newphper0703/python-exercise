#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 14:56
# @Author  : LiuZhi
# @Site    : 
# @File    : recursionFunction.py
# @Software: PyCharm

#使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(1))
print(fact(5))
print(fact(100))
#print(fact(1000))

#尾递归优化
def factTwo(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num*product)

#python 汉诺塔
def move(n, a,b,c):
    if n == 1:
        print(a,'-->',c)
        return
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

print(move(3, 'a', 'b', 'c'))