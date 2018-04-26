#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 11:38
# @Author  : LiuZhi
# @Site    : 
# @File    : CustomClass.py
# @Software: PyCharm

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__

print(Student('Michael'))