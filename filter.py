#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 15:26
# @Author  : LiuZhi
# @Site    : 
# @File    : filter.py
# @Software: PyCharm
def is_odd(n):
    return n%2 == 1

print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['a', '', 'b', None, 'C', ' '])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x : x % n >0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数
def is_palindrome(n):
    pass

