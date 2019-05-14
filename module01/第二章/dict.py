#Author:Timmy
dic = {'k1':'v1','k2':'v2','k3':'v3'}

#1 循环遍历所有的key
# for k in dic:
#     print(k)

#2 循环遍历出所有的value
# for k in dic:
#     print(dic.get(k))

#3 循环遍历出所有的key和value
# for k in dic:
#     print(k+':'+dic.get(k))

#4 添加一个键值对，'k4':'v4'，输出添加后的字典
# dic['k4'] = 'v4'
# print(dic)

#5 删除一个键值对，'k1':'v1'，输出删除后的字典
# dic.pop('k1')
# print(dic)

#6 删除字典中k5对应的键值对，如果字典中不存在'k5'键，返回None
# print(dic.pop('k5',None))

#7 获取k2对应的值
# print(dic['k2'])

#8 获取字典中k6对应的值，如果不存在，则不报错，并且让其返回None
print(dic.get('k6',None))

#9 现有dic2 = {'k1':'v111','a':'b'},通过一行操作是dic2 = {'k1':'v1','k2':'v2','k3':'v3','a':'b'}
# dic2 = {'k1':'v111','a':'b'}
# dic2.update(dic)
# print(dic2)
#注意，字典是无序的，所以顺序可能和题目要求不同

# 10 组合嵌套题。写代码，有如下列表，按照要求实现每一个功能
    #lis = [[‘k’,[‘qwe’,20,{‘k1’:[‘tt’,3,’1’]},89],’ab’]]
    #1.将列表中的lis中的‘tt’变成大写（用两种方法）
    #2.将列表中的数字3变成字符串‘100’，用两种方法
    #3.将列表中的字符串'1'变成数字'101',用两种方式
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
# lis[0][1][2]['k1'][0]=lis[0][1][2]['k1'][0].upper()
# print(lis)
# lis[0][1][2]['k1'][0] = 'TT'
# print(lis)

