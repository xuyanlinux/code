# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/19
from collections import  Iterable
from collections import  Iterator
lis1 = list(range(5))
print(isinstance(lis1,Iterable))
print(isinstance(lis1,Iterator))
print(isinstance(iter(lis1),Iterator))
