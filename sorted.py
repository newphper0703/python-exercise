#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 16:24
# @Author  : LiuZhi
# @Site    : 
# @File    : sorted.py
# @Software: PyCharm

print(sorted([36, 5, -12, 9, -21]))
print(sorted([36, 5, -12, 9, -21], key = abs))
#对字符串排序，是按照ASCII的大小比较的
print(sorted(['bob', 'about', 'Zoo', 'Credit', 'HHH', 'jjG']))

print(sorted(['bob', 'about','Zoo', 'Credit'], key = str.lower))
print(sorted(['bob', 'about','Zoo', 'Credit'], key = str.lower, reverse=True))

#by_name
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#by_score_desc
