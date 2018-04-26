#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 10:36
# @Author  : LiuZhi
# @Site    : 
# @File    : Property.py
# @Software: PyCharm

#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())
#s.set_score(9999)
#print(s.get_score())

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value,  int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018-self._birth


s = Student()
s.score = 60
print(s.score)