#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 17:21
# @Author  : LiuZhi
# @Site    : 
# @File    : Anonymous.py
# @Software: PyCharm

print(list(map(lambda x :x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def f(x):
    return x * x

f = lambda x:x*x
#print(f)
print(f(5))

def build(x, y):
    return lambda: x*x + y*y

print(build(1, -1)())
print(build(2, 2)())
