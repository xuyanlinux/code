#Author:Timmy
class luffystudent:
    school = "luffycity"
    def __init__(self,name,gender,age):
        self.Name = name
        self.Gender = gender
        self.Age = age

    def learn(self):
        print("%s is learning..." %(self.Name))
    def eat(self):
        print("%s is eatting..."%(self.Name))
    def sleep(self):
        print("%s is sleeping..."%(self.Name))


#生成对象
stu1 = luffystudent('huhu','男',6)
stu2 = luffystudent('xuyan','男',31)

'''
下面语句输出
{'Name': 'huhu', 'Gender': '男', 'Age': 6}
{'Name': 'xuyan', 'Gender': '男', 'Age': 31}
'''
# print(stu1.__dict__)
# print(stu2.__dict__)



'''
下面语句输出：
luffycity 1622054216752
luffycity 1622054216752
id相同说明不同实例的数据属性是共享的
'''
# print(stu1.school,id(stu1.school))
# print(stu2.school,id(stu2.school))



'''
下面语句输出：
huhu is sleeping...
None 1667312522760
xuyan is sleeping...
None 1667312522760
id不同，说明每个实例的函数属性是不用的；
我们没有传递参数，对象把自己传递给了类中的sleep函数
'''
print(stu1.sleep(),id(stu1.sleep))
print(stu2.sleep(),id(stu2.sleep))


