#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 11:33
# @Author  : LiuZhi
# @Site    : 
# @File    : ClassAndInstance.py
# @Software: PyCharm
#面向对象最重要的概念就是类（Class）和实例（Instance），
# 必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。

class Student(object):
    #pass
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(std):
        print('%s : %s' % (std.name, std.score))
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

'''bart = Student()

print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)
'''
bart = Student('Bart Simpson', 59)
print(bart.name)
print(bart.score)
bart.print_score()
lisa = Student('Lisa', 99)
print(bart.name, bart.get_grade())
print(lisa.name, lisa.get_grade())
#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
bart.age = 8
print(bart.age)
print(lisa.age)