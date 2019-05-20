# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/18


list_account = []
list_key = ['Name','Password','FuLL Name','Age','Job','Profession','Tel']
dic_account = {}
f = open(file='account.txt',mode='r',encoding='utf-8')
for line in f:
    lis1 = line.split(',')
    list_account.append(dict(zip(list_key,lis1)))
f.close()

print(list_account)
