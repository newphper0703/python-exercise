#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 11:11
# @Author  : LiuZhi
# @Site    : 
# @File    : MultiExtends.py
# @Software: PyCharm

#Python允许使用多重继承，因此，MixIn就是一种常见的设计。
class Animal(object):
    pass
class Runnable(object):
     def run(self):
         print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass