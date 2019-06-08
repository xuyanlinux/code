# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/27
import re
a = re.compile("""\d + # the integral part
                \. # the decimal point
                \d * # some fractional digits""",
                re.X)
b = re.compile('(\d+)\.(\d+)')
print(a)
c = a.search(r'abc123.345d')
print(c.groups())
d = b.search('abc123.345d')
print(d.groups())
