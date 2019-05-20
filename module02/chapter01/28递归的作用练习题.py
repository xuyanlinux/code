# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/17

# data = [1, 3, 6, 7, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 30, 32, 33, 35]
data = list(range(100))
# print(data)


def find(lis,n):
    index_mid = len(lis)//2
    if n == lis[index_mid]:
        return index_mid
    elif n < lis[index_mid]:
        return index_mid - find(lis[0:index_mid],n) - 1
    else:
        return find(lis[index_mid+1:],n) + index_mid + 1

print(find(data,80))


