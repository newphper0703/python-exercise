#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 16:17
# @Author  : LiuZhi
# @Site    : 
# @File    : GetInsatnce.py
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


print(type(123))
print(type('str'))
print(type(None))

print(type(abs))
print(type(123) == type(456))
print(type(123) == int)
print(type('456') == type(123))

import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

a = Animal()
d = Dog()
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(d, Animal) and isinstance(d, Dog))
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))
print(dir('abc'))
print('abc'.__len__())

class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print(obj)
print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(hasattr(obj, 'y'))
print(getattr(obj, 'y'))
print(obj.y)
#print(getattr(obj, 'z'))
print(getattr(obj, 'z', 404))
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')
print(fn)
print(fn())

#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
#Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
def readImage(fp):
    if hasattr(fp, 'read'):
        pass
        #return readData(fp)
    return None

