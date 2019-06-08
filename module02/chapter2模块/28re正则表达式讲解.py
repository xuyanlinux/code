# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/26
import re
f = open(file="兼职白领学生空姐模特护士联系方式.txt",mode='r',encoding='GBK')

data = f.readlines()

print(data)

# print(re.findall("[0-9]{11}",data))