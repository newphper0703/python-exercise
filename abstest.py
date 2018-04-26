#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 16:17
# @Author  : LiuZhi
# @Site    : 
# @File    : abstest.py
# @Software: PyCharm
'''
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x