#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 14:10
# @Author  : LiuZhi
# @Site    : 
# @File    : AccessControl.py
# @Software: PyCharm

class Student(object):
    #pass
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def print_score(self):
        #在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        #在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
        print('%s : %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0<= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    def get_gender(self):
        return self.__gender
    def set_gender(self, gender):
        if gender == 'male' | gender == 'female':
            self.__gender = gender
        else :
            raise ValueError('bad gender')


    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59, 'male')
#print(bart.__name)
print(bart._Student__name)
print(bart.get_name())
print(bart.get_score())
bart.__name = 'new name'
print(bart.__name)
print(bart.get_name())
bart.__gender = 'hhhhh'
print(bart.__gender)
print(bart.get_gender())