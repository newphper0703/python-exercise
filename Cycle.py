#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 14:11
# @Author  : LiuZhi
# @Site    : 
# @File    : Cycle.py
# @Software: PyCharm
'''names = ['jane','bob', 'mark']
for name in names:
    print(name)
 '''
'''
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum+x
print(sum)
'''
'''
#0-100的整数之和
sum = 0
for x in range(10):
    sum = sum + x
print(sum)
print(list(range(5)))
'''
'''
#要计算100以内所有奇数之和
sum = 0
n = 99
while n > 0 :
    sum = sum +n
    n = n - 2
print(sum)
'''
'''
L = ['BART', 'LISA', 'ADAM']
for name in L:
    print('Hello,', name, '!')
'''
'''
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')
'''
'''
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
'''
#break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
n = 0
while n < 10:
    n = n + 1
    print(n)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
