#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 18:10
# @Author  : LiuZhi
# @Site    : 
# @File    : Attribute.py
# @Software: PyCharm

class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90

class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'liuzhi'
s.age = 25
#s.score = 100

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 9999
