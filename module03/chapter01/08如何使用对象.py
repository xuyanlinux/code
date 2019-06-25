#Author:Timmy
class luffystudent:
    school = "luffycity"
    def __init__(self,name,gender,age):
        self.Name = name
        self.Gender = gender
        self.Age = age

    def learn(self):
        print("is learning...")
    def eat(self):
        print("is eatting...")
    def sleep(self):
        print("is sleeping...")

stu1 = luffystudent('huhu','男','6')    # 下面生成的变量在实例stu1的名字空间
print(stu1.__dict__)                     #  输出{'Name': 'huhu', 'Gender': '男', 'Age': '6'}
print(stu1.Name)
print(stu1.Gender)
print(stu1.Age)
