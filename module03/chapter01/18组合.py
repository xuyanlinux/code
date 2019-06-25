#Author:Timmy

class People:
    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age

class Teacher(People):
    def __init__(self,name,sex,age,course,salary):
        People.__init__(self,name,sex,age)
        self.Course = course
        self.Salary = salary
        self.course = []
    def teach(self):
        print("%s is teaching..."%(self.Name))


class student(People):
    def __init__(self,name,sex,age,course,course_time):
        People.__init__(self,name,sex,age)
        self.Course = course
        self.Course_time = course_time
        self.course = []
    def teach(self):
        print("%s is studing..."%(self.Name))

teacher1 = Teacher('gongyu','femail',22,'vv','1000')
print(teacher1.Salary)

class course:
    def __init__(self,course_name,course_period,course_price):
        self.Name = course_name
        self.Period = course_period
        self.Price = course_price
    def info(self):
        print("课程名：%s     课程周期：     %s       课程价格：      %s"%(self.Name,self.Period,self.Price))

python = course('python','6mons',7000)
linux = course('linux','5mons',6000)
# print(course1.__dict__)

teacher1.course.append(python)
teacher1.course.append(linux)
for i in teacher1.course:
    i.info()