#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = (1,2,3)
print(classmates)
print(classmates[0])
t=()
print(t)
print(len(t))
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

s = (1, 2 , [3,4])
print(s)
s[2][0] = 5
s[2][1] = 6
print(s)
