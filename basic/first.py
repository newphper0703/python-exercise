#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print('I','love', 'China')
print(100+200)
print('100+200=', 100+200)
print(3>2)
print(True)
print(False)
print('中文字符串')
print(ord('A'))
print(ord('a'))
print(ord('中'))
print(chr(97))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#print(b'\xe4\xb8\xad\xff'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(r'\\\t\\')
print('''l1 
l2 
l3''')

#len()函数计算的是str的字符数
print(len('中文'))
print(len('ac'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
print("i 'm \"ok\" ! \n thank you !")

print('hello , %s' % 'world')
print('hi, %s, you have $%d' %('mike', 100000))
print('age : %s. gender: %s' % (25, True))
print('growth rate:%d %%' % 7)
print('hello ,{0}, 成绩提升了 {1:.1f}%'.format('晓明', 17.125))
print('hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', (85-72)/72*100))
a = 100
if a>=0 :
    print(a)
else :
    print(-a)
name = input('enter your name:')
print('hello', name)





