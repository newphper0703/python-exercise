#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''age = 20
if age >= 18:
    print('your age is ', age)
    print('adult')
'''
'''age =3
if age >=18:
    # print('your age is', age)
    print('adult')
elif age >=6 :
    # print('your age is', age)
    print('teenager')
else:
    print('kid')
'''
'''
s = input('birth:')#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数
birth = int(s)
if birth > 2000:
    print('00后')
else:
    print('00前')
'''
#
height = 1.75
weight = 80.5
bmi = weight/(height*height)
if bmi < 18.5:
    print('过轻')
elif (bmi >= 18.5 and bmi< 25):
    print('正常')
elif (bmi >= 25 and bmi< 28):
    print('过重')
elif (bmi >= 28 and bmi <= 32):
    print('肥胖')
else :
    print('严重肥胖')