#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 15:27
# @Author  : LiuZhi
# @Site    : 
# @File    : Slice.py
# @Software: PyCharm
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3
print(L[0:3])
#如果第一个索引是0，还可以省略
print(L[:3])
print(L[1:3])
#Python支持L[-1]取倒数第一个元素
print(L[-2:])
print(L[-2:-1])
l = list(range(100))
print(l[:10])
print(l[-10:])
print(l[:10:2])
print(l[::5])
print(l[:])
print((0,1,2,3,4,5)[:3])
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

def trim(str):
    while str[:1] == ' ':
        str = str[1:]
    while str[-1:] == ' ':
        str = str[:-2]
    return str

print(trim('    aaa hh welcome    '))