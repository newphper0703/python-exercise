#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 11:17
# @Author  : LiuZhi
# @Site    : 
# @File    : Oop.py
# @Software: PyCharm
std1 = {'name':'Michael', 'score':98}
std2 = {'name':'Bob', 'score': 81}

def print_score(std):
    print('%s : %s' % (std['name'], std['score']))

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s : %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
