#Author:Timmy


"""
方法1：指名道姓

"""""



'''
方法2：super()
'''


class A:
    def f1(self):
        print("from A")
        super(A, self).f1()

class B:
    def f1(self):
        print("from B")

class C(A,B):
    pass

print(C.mro())  # 输出[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

c = C()
c.f1()
'''
输出：
from A
from B
说明super()是顺着mro表往后找的，而不是找A类的父类
'''

