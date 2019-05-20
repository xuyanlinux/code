# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/19

def fib(n):
    count,a,b = 0,0,1
    while count < n:
        print('before yield')
        sign = yield b
        if sign == 'stop':
            break

        a,b = b,a+b
        count += 1


s = fib(15)
print(next(s))
print(s.send(None))
print(s.send('stop'))

