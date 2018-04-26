#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 16:53
# @Author  : LiuZhi
# @Site    : 
# @File    : Comprehensions.py
# @Software: PyCharm

#列表生成式
print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x*x)

print(L)

print([x*x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x%2 == 0])

print([m+n for m in 'ABC' for n in 'XYZ'])

import os# 导入os模块，模块的概念后面讲到
print([d  for d in os.listdir('.')])# os.listdir可以列出文件和目录

d = {'x':'a', 'y':'b', 'z':'c'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'Python', 'PYTHON']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str) == True])