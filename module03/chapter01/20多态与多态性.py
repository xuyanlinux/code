#Author:Timmy

# 动态多态性

# import abc
# class animal:
#     @abc.abstractmethod
#     def call(self):
#         pass
# class people(animal):
#     def call(self):
#         print("hello")
# class dog(animal):
#     def call(self):
#         print("wangwang")
# class cat(animal):
#     def call(self):
#         print("miaomiao")
# peo1 = people()
# dog1 = dog()
# cat1 = cat()
#
# def call(object):
#     object.call()
# call(peo1)
# call(cat1)
# call(dog1)


#鸭子类型：你长得像鸭子，走路像鸭子，叫声像鸭子，那么你就是鸭子

# class disk():
#     def read(self):
#         print("disk read")
#     def write(self):
#         print("disk write")
# class text:
#     def read(self):
#         print("text read")
#     def write(self):
#         print("text write")
# dis1 = disk()
# text1 = text()
# def read(object):
#     object.read()
#     object.write()
# read(dis1)
# read(text1)

print(list.__dict__)
l1 = list([1,2,3,4])
s1 = str('hello')
t1 = tuple((4,5,6))

print(l1.__len__())
# def len(object):
#     return object.__len__()

print(len(l1),len(s1),len(t1))