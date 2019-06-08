# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/24
import random,string

a = ''.join(random.sample(string.ascii_letters + string.punctuation + string.digits,15))
print(a)
