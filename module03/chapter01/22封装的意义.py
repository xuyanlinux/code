#Author:Timmy
class Teacher:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def tell_info(self):
        print('姓名:%s,年龄:%s' %(self.__name,self.__age))
    def set_info(self,name,age):
        if not isinstance(name,str):
            raise TypeError('姓名必须是字符串类型')
        if not isinstance(age,int):
            raise TypeError('年龄必须是整型')
        self.__name=name
        self.__age=age

t=Teacher('egon',18)
t.tell_info()

t.set_info(22,19)
t.tell_info()

