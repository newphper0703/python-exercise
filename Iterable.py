#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 19:45
# @Author  : LiuZhi
# @Site    : 
# @File    : Iterable.py
# @Software: PyCharm

from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter('ABC'), Iterator))