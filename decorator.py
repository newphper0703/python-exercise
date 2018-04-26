#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 17:55
# @Author  : LiuZhi
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm
def now():
    print('2018-04-16')

f = now
print(f())

print(now.__name__)
print(f.__name__)

def log(func):
    def warpper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return warpper

@log
def now():
    print('2018-04-16')

print(now())

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s ():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2018-04-16')

print(now())
print(now.__name__)


import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s ():' % func.__name__)
        return func(*args, **kw)
    return wrapper

