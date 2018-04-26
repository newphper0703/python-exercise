#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 16:29
# @Author  : LiuZhi
# @Site    : 
# @File    : Iteration.py
# @Software: PyCharm
#迭代
d= {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for ch in 'ABD':
    print(ch)

from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

for x, y in [(1,1), (2, 4), (3,9)]:
    print(x, y)

def findMinAndMax(L):
    return None,None
