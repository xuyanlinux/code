#Author:Timmy

li = ['alex','egon','yuan','wusir','666']

##1、把666换成999
li[-1] = '999'
print(li)

##2、获取‘yuan’索引
print(li.index('yuan'))

##3、假设不知道前面有几个元素，分片得到最后的三个元素
print(li[-3:])




