#Author:Timmy

class School:
    def __init__(self,city):
        self.city = city
        self.course = []
        self.gender = []

class People():
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

class Teacher(People):
    def __init__(self,name,sex,age):
        super(Teacher, self).__init__()
        self.school = []


class student(People):
    def __init__(self,name,sex,age):
        super(student, self).__init__()
        self.school = []
        self.gender = []
    def register(self):
        print("%s 注册成功"% self.name)
    def pay(self):
        print("$s 缴费成功"% self.name)
    def choice_gender(self,gender_obj):
        self.gender.append(gender_obj)


class Gender(School):
    def __init__(self,name):
        self.name = name
        self.course = []


class Course():
    def __init__(self,name,period,price):
        self.name = name
        self.period = period
        self.price = price

python = Course('Python','6mons',8888)
linux = Course('Linux','4mons',6666)
go = Course('Go','2mons','1680')

c1 = School('北京')
c2 = School('上海')

c1.course.append(python)
c1.course.append(linux)
c2.course.append(go)

