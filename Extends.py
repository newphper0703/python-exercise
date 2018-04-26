#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 14:37
# @Author  : LiuZhi
# @Site    : 
# @File    : Extends.py
# @Software: PyCharm

class Animal(object):
    def run(self):
        print('Animal is running ...')

class Dog(Animal):
    #pass
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    #pass
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Animal()))
print(run_twice(Dog()))

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

print(run_twice(Tortoise()))

#开闭原则：对扩展开发，对修改封闭
class Timer(object):
    def run(self):
        print('Start...')




