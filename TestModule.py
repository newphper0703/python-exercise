#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 10:24
# @Author  : LiuZhi
# @Site    : 
# @File    : TestModule.py
# @Software: PyCharm

__author__ = 'liuzhi'
import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World!')
    elif len(args) == 2:
        print('Hello , %s' % args[1])
    else :
        print('Too many arguments!')


if __name__=='__main__':
    test()