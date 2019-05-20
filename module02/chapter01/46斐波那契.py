# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/18

# lis1 = [i for i in range(5)]
# lis_fib = []

# def fib(n):
#     count,a,b = 0,0,1
#     while count < n:
#         print(b)
#         a,b = b,a+b
#         count += 1
#
# fib(15)

# 根据上面的函数写生成器


def fib(n):
    count,a,b = 0,0,1
    while count < n:
        print('before yield')
        yield b
        a,b = b,a+b
        count += 1


f = fib(15)
for i in f:
    print(i)