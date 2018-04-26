#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = [1,2,3]
print(classmates)
print(len(classmates))
print(classmates[0])
#索引超过范围
#print(classmates[3])
#获取最后一个元素
print(classmates[-1])
classmates.append(4)
print(classmates)
classmates.insert(1,3)
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
#只能用于元素替换
classmates[1] = 'hello'
print(classmates)
#list里面的元素的数据类型也可以不同
p = [True, '3uuu', 4]
classmates.insert(3, p)
print(classmates)
q = []
print(len(q))