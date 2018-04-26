#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 14:59
# @Author  : LiuZhi
# @Site    : 
# @File    : DictAndSet.py
# @Software: PyCharm
'''
dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

1.查找和插入的速度极快，不会随着key的增加而变慢；
2.需要占用大量的内存，内存浪费多。
而list相反：

1.查找和插入的时间随着元素的增加而增加；
2.占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict的key必须是不可变对象
'''
'''
d = {'a':1,'b':2,'c':3,'d':4}
print(d['a'])
d['e'] = 5
print(d)
d['f'] = 6
print(d['f'])
d['f'] = 7
print(d['f'])
#print(d['g'])
print('g' in d)
print(d.get('g'))
print(d.get('g', 8))
print(d)
d.pop('f')
print(d)
'''

'''
key = [1, 2, 3]
d[key] = 'a list'
print(d)
'''

'''
在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
'''
s = set([1,2,3])
print(s)
s= set([1, 2, 2, 3, 3, 4])
print(s)
s.add(5)
print(s)
s.add(5)
print(s)
s.remove(5)
print(s)
s1= set([1,2,3])
s2= set([2,3,4])
print(s1 & s2)
print(s1 | s2)

a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
print(a.replace('a', 'A'))
print(a)

'''
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
'''
a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

