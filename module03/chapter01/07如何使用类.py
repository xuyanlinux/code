#Author:Timmy

class luffystudent:
    school = "luffycity"
    def learn(self):
        print("is learning...")
    def eat(self):
        print("is eatting...")
    def sleep(self):
        print("is sleeping...")

#查
print(luffystudent.__dict__)               # 查看类的字典结构
print(luffystudent.__dict__['school'])
print(luffystudent.school)                 # 这种方法是查看属性的常用方法，和上面的语句效果一样
print(luffystudent.learn("dd"))

#增
luffystudent.country = "China"
print(luffystudent.country)

#删
del luffystudent.country


#改
luffystudent.school = 'oldboy'
print(luffystudent.school)

