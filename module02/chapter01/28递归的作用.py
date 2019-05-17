# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/17

##计算4的阶乘


def  factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

result = factorial(4)
print(result)