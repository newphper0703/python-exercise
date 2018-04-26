#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 18:18
# @Author  : LiuZhi
# @Site    : 
# @File    : generator.py
# @Software: PyCharm

L = [x*x for x in range(10)]
print(L)
g = (x*x for x in range(10))
#print(g)
#print(next(g))

for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0,  1
    while n < max:
        print(b)
        #yield b
        a, b = b, a+b
        n = n+1
    return 'done'

print(fib(6))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o))

g = fib(6)
while True:
    try:
        x = next(g)
        print('g：', x)
    except StopIteration as e :
        print('Generator return value:', e.value)
        break

#杨辉三角
def triangles():
    pass
