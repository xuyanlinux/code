# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/17

# a = (1,4,5,-3)
# print(min(a))
#
# for index,value in enumerate(a):
#     print(index,value)
# eval()

#print(pow(2,3))

lis = list(range(9))
lis2 = list(range(5))
# print(lis)

# res1 = map(lambda x:x*x,lis)
# print(list(res1))
#
# res2 = filter(lambda x:x > 5,lis)
# print(list(res2))

f = open(file='print_2_file.txt',mode='w',encoding='utf-8')
print('HELLLO WORLD','你好，世界',sep='!',end='\n',file=f)
f.close()
callable()