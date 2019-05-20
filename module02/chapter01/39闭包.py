# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/18


def func():
    n = 10

    def func1():
        print('func1:',n)
    return func1


print(func())
f = func()
f()
