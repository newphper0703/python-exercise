#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 16:07
# @Author  : LiuZhi
# @Site    : 
# @File    : Function.py
# @Software: PyCharm

#求绝对值的函数
print(abs(100))
print(abs(-20))
print(abs(12.34))

#print(abs(1,2))
#print(abs('q'))

print(max(1,2))
print(max(1,2,3,-5))

print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

a = abs
print(a(-1))

n1 = 255
n2 = 1000
print(hex(255))
print(hex(1000))


from abstest import my_abs
print(my_abs(-2))
#print(my_abs(-2,3))
#print(my_abs('222'))
'''
pass用法
def nop():
    pass

age = 26
if age >= 18:
    pass
'''
import math

def move(x,y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x, y = move(100, 100, 60, math.pi/6)
print(x,y)
r = move(100, 100, 60, math.pi/6)
print(r)

#求一元二次方程的根
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a is not a number')
    if not isinstance(b, (int, float)):
        raise TypeError('a is not a number')
    if not isinstance(c, (int, float)):
        raise TypeError('a is not a number')
    d = b*b - 4*a*c
    if a == 0:
        if b == 0:
            if c == 0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1 = -c/b
            x2 = x1
            return x1, x2
    else:
        if d<0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(d))/2/a
            x2 = (-b - math.sqrt(d))/2/a
            return x1,x2
print(quadratic(2, 3, 1))
print(quadratic(0,0,0))

def power(x):
    return x*x

print(power(4))
print(power(-2))

#默认参数
def powerThree(x, n=2):
    s = 1
    while n >0 :
        n = n - 1
        s = s * x
    return s

print(powerThree(5,3))
print(powerThree(5))

def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:', name)
    print('gender', gender)
    print('age', age)
    print('city', city)
print(enroll('Sarah', 'F'))

def add_end(l=None):
    if l is None:
        l = []
    l.append('END')
    return l
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())

#可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum  = sum + n * n
    return sum

print(calc([1, 2, 3]))
print(calc((1, 2, 3)))

def calcTwo(*numbers):
    sum = 0
    for n in numbers:
        sum  = sum + n * n
    return sum

print(calcTwo(1,2))
print(calcTwo())
numbers = [1, 2, 3]
print(calcTwo(numbers[0], numbers[1], numbers[2]))
print(calcTwo(*numbers))

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('michael', 30)
person('michael', 30, city='Beijing')
person('michael', 30, gender='m', job='engineer')
extra = {'city':'Beijing', 'job': 'engineer'}
person('Jack', 24, city = extra['city'], job = extra['job'])
person('Jack', 24, **extra)

def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('jack', 24, city='beijing', addr = 'chaoyang', zipcode=123456)
def personTwo(name, age, *, city, job):
    print(name, age, city, job)
personTwo('jack', 24, city='beijing', job='engineer')
def personThree(name, age, *args, city, job):
    print(name, age, args, city, job)
#personThree('jack', 24, 'beijing', 'engineer')
def personFour(name, age, *, city='beijing', job):
    print(name, age, city, job)
personFour('jack', 24,  job = 'engineer')
def personFive(name, age, city, job):
    pass
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)
f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1,2, 3, 4)
kw = {'d':99,'x':'#'}
f1(*args, **kw)

args = (1,2, 3)
kw = {'d':88, 'x':'#'}
f2(*args, **kw)


