#! _*_ coding:utf-8 _*_
import pickle
import os
courseinfo = 'course.info'
gradeinfo = 'grade.info'
studentinfo = 'student.info'
teacherinfo = 'teacher.info'
userinfo = 'user.info'
admin_passwd = '123456'
managerinfo = 'manager.info'
class Base:
    @staticmethod
    def getinfo_from_file(path):
        if os.path.isfile(path):
            with open(path, mode='rb') as f:
                while True:
                    try:
                        data = pickle.load(f)
                        yield data
                    except:
                        break
        else:
            print("没有发现文件")

    @staticmethod
    def dumpinfo_to_file(path,obj):
        with open(path, mode='ab') as f:
            pickle.dump(obj,f)
            f.flush()

    def modify_file(self,path):
        f_sou = open(path,mode='rb')
        f_bak = open(path+'.bak',mode='wb')
        while True:
            try:
                obj= pickle.load(f_sou)
                if obj.name == self.name:
                    pickle.dump(self,f_bak)
                else:
                    pickle.dump(obj,f_bak)
            except:
                break
        f_bak.close()
        f_sou.close()
        os.remove(path)
        os.rename(path+'.bak',path)




    @staticmethod
    def show_courseinfo():
        for sn,course_obj in enumerate(Base.getinfo_from_file(courseinfo),1):
            print(sn,repr(course_obj))

    @staticmethod
    def show_schoolinfo():
        school_list = ['北京校区','上海校区']
        for sn,school_name in enumerate(school_list,1):
            print(sn,school_name)

    @staticmethod
    def show_gradeinfo():
        for sn,grade_obj in enumerate(Base.getinfo_from_file(gradeinfo),1):
            print(sn,repr(grade_obj))

    @staticmethod
    def show_teacherinfo():
        for sn,te_obj in enumerate(Base.getinfo_from_file(teacherinfo),1):
            print(sn,repr(te_obj))

    @staticmethod
    def show_studentinfo():
        for sn,stu_obj in enumerate(Base.getinfo_from_file(studentinfo),1):
            print(sn,repr(stu_obj))

class School():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        info = "学校名称：%s"%self.name
        return info
    def create_course(self,name,period,price):
        school = self.name
        course1 = Course(school,name,period,price)
        Base.dumpinfo_to_file(courseinfo,course1)
    def create_grade(self,name,course,teacher_list):
        return Grade(name,self.name,course,teacher_list)

# 创建北京、上海两所学校
school_bj = School('北京分校')
school_sh = School('上海分校')



class Course:
    def __init__(self,school,name,period,price):
        self.school = school
        self.name = name
        self.period = period
        self.price = price
    def __str__(self):
        dic_info = {'name': self.name,'school':self.school, 'period': self.period, 'price': self.price}
        info = '''
        ---------------info of %(name)s---------------
        课程名称:%(name)s
        所在学校：%(school)s
        课程周期：%(period)s
        课程价格：%(price)s
        '''.strip() % (dic_info)
        return info
    def __repr__(self):
        return '|'.join([self.name,self.school,self.period,self.price])
class Grade:
    def __init__(self,name,school_name,course,teacher_list):
        self.name = name
        self.school = school_name
        self.course = course
        self.teacher_list = teacher_list
    def __repr__(self):
        return '|'.join([self.name.ljust(10),self.school,self.course])

class People:

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def menu(self):
        while True:
            s = ("%s----%s功能菜单"%(self.role,self.name)).center(50,'*')
            print('\033[1;34;0m%s\033[0m'%s)
            for index,action in enumerate(self.menu_list):
                print(index,action)
            choice_index = input("请选择功能，输入功能编号,或者输入q|Q退出登录").strip()
            if choice_index.upper() == 'Q':
                break
            elif choice_index.isdigit():
                choice_index = int(choice_index)
                if choice_index >= 0 and choice_index < len(self.menu_list):
                    func = getattr(self,self.menu_list[choice_index])
                    func()
                else:
                    print("没有编号为%s的功能"%choice_index)
            else:
                print("只可以输入数字")


class Studente(People,Base):
    menu_list = ["select_grade","check_grade"]
    role = 'Studente'
    def __init__(self,name,age,sex):
        People.__init__(self,name,age,sex)
        self.grade_list = []
        self.score_dic = {}
    @staticmethod
    def sign():
        print("开始注册".center(50,'+'))
        name = input("输入学生姓名>>>").strip()
        if os.path.exists(teacherinfo):
            for obj in Base.getinfo_from_file(teacherinfo):
                if obj.name == name:
                    print("\033[1;31;0m%s已经注册过了\033[0m"%name)
                    return
        password = input("输入密码：").strip()
        age = int(input("输入学生年龄>>>").strip())
        sex = input("输入学生性别>>>").strip()
        sign_info = '|'.join([name,password,'student'])
        Base.dumpinfo_to_file(userinfo,sign_info)
        stu1 = Studente(name,age,sex)
        Base.dumpinfo_to_file(studentinfo,stu1)
    def pay(self,amount):
        print('确认付款金额：%s 元'%(amount))
        action = input("是否付款：y|Y表示付款，其他输入表示不付款>>>").strip()
        if action.upper() == 'Y':
            print("缴费成功")
            return 1
        else:
            print("缴费失败")
            return 0
    def select_grade(self):
        print("开始选课".center(50, '+'))
        Base.show_gradeinfo()
        grade_num = int(input("输入你要选择的班级编号").strip())
        grade_obj_gen = Base.getinfo_from_file('grade.info')
        flag = 0
        for index,grade_obj in enumerate(grade_obj_gen,1):
            if index == grade_num:
                grade = grade_obj.name
                flag = 1
                course_name = grade_obj.course
                for obj in Base.getinfo_from_file(courseinfo):
                    if course_name == obj.name:
                        amount = obj.price
        if flag == 0:
            print("输入的班级编号有误")
            return
        pay_result = self.pay(amount)
        if pay_result == 1:
            self.grade_list.append(grade)
            self.score_dic[grade] = 0
            self.modify_file(studentinfo)
            print("选课成功")
        else:
            print("缴费失败。。请重新选课并缴费")
            return
    def check_grade(self):
        print("已选课程：")
        for index,grade in enumerate(self.grade_list):
            print(index,grade)

    def __str__(self):
        info = '''
            name:%s
            age:%s
            sex:%s
            role:%s
            grade_list:%s
            score_list:%s
            '''%(self.name,self.age,self.sex,self.__role,self.grade_list,self.score_list)
        return info

    def __repr__(self):
        info = '|'.join([self.name.ljust(10),str(self.age),self.sex,str(self.grade_list),str(self.score_dic)])
        return info
class Teacher(People):
    role = 'Teacher'
    menu_list = ["select_grade", "print_stu_list", "modify_score"]
    def __init__(self,name,age,sex,school_list):
        People.__init__(self,name,age,sex)
        self.school_list = school_list

    '''
    功能：查看执教班级
    '''
    def check_grade(self):
        print("执教班级".center(50, '='))
        grade_list = []
        for sn, grade_obj in enumerate(Base.getinfo_from_file(gradeinfo), 1):
            if self.name in grade_obj.teacher_list:
                grade_list.append(grade_obj.name)
        for sn, grade_name in enumerate(grade_list, 1):
            print(sn, grade_name)
        return grade_list

    '''
    功能：选择班级
    '''
    def select_grade(self):
        grade_list = self.check_grade()
        choice_grade_num = input("选择班级编号>>>").strip()
        if choice_grade_num.isdigit():
            choice_grade_num = int(choice_grade_num)
            choice_grade = grade_list[choice_grade_num - 1]
        print("已选择班级：%s"%(choice_grade))
        return choice_grade

    '''
    功能：查看班级学员列表：
    '''
    def print_stu_list(self):
        choice_grade_name = self.select_grade()
        stu_list = []
        for obj in Base.getinfo_from_file(studentinfo):
            if choice_grade_name in obj.grade_list:
                stu_list.append(obj.name)
        for num,name in enumerate(stu_list,1):
            print(num,name)

        return stu_list,choice_grade_name
    '''
    功能：修改学员分数
    '''
    def modify_score(self):
        stu_list,grade_name = self.print_stu_list()
        stu_index = input("选择学生编号>>>").strip
        stu_index = int(stu_index)
        stu_name = stu_list(stu_index - 1)

        for obj in Base.getinfo_from_file(studentinfo):
            if obj.name == stu_name:
                obj.score_dic[grade_name] = score
                obj.modify_file(studentinfo)

    def show_info(self):
        dic_info = {'name':self.name,'age':self.age,'sex':self.sex,'school_list':self.school_list}
        info = '''
        ---------------info of %(name)s---------------
        姓名:%(name)s
        年龄：%(age)s
        性别：%(sex)s
        任教学校：%(school_list)s
        '''.strip() % (dic_info)
        print(info)
    def __str__(self):
        dic_info = {'name': self.name, 'age': self.age, 'sex': self.sex, 'school_list': self.school_list}
        info = '''
        ---------------info of %(name)s---------------
        姓名:%(name)s
        年龄：%(age)s
        性别：%(sex)s
        任教学校：%(school_list)s
        '''.strip() % (dic_info)
        return info
    def __repr__(self):
        return '|'.join([self.name.ljust(10),str(self.age),self.sex,str(self.school_list)])

class Manager(People):
    menu_list = ["create_te", "create_grade", "create_course","show_te_list","show_stu_list","show_course_list","show_grade_list"]
    role = 'Manager'
    def create_te(self):
        name = input("教师姓名：").strip()
        if os.path.exists(teacherinfo):
            for obj in Base.getinfo_from_file(teacherinfo):
                if obj.name == name:
                    print("\033[1;31;0m%s老师已经被创建\033[0m"%name)
                    return
        passwd = input("登录密码").strip()
        te_info = name+'|'+passwd+'|'+'teacher'
        Base.dumpinfo_to_file(userinfo,te_info)
        age = input("教师年龄：").strip()
        if age.isdigit():
            age = int(age)
        else:
            print("年龄只能是数字!")
            return
        sex_num = input("教师性别编号，1：male；2：female").strip()
        if sex_num == '1':
            sex = 'M'
        elif sex_num == '2':
            sex = 'F'
        else:
            print('输入的性别编号有错！')
            return
        school_num =  input("输入任教学校编号，1：北京；2：上海；3：北京和上海：").strip()
        if school_num == '1':
            school_list = [school_bj.name]
        elif school_num == '2':
            school_list = [school_sh.name]
        elif school_num == '3':
            school_list = [school_bj.name,school_sh.name]
        else:
            print("输入的学校编号有错！")
            return
        te = Teacher(name,age,sex,school_list)
        te.school_list = school_list
        Base.dumpinfo_to_file(teacherinfo,te)
    def create_grade(self):
        print("开始创建班级".center(50,'-'))
        name = input("输入班级名称：").strip()
        if os.path.exists(gradeinfo):
            for obj in Base.getinfo_from_file(gradeinfo):
                if obj.name == name:
                    print("\033[1;31;0m已有%s课程\033[0m"%name)
                    return

        print("为班级选关联课程，课程列表".center(50,'='))
        if not os.path.exists(courseinfo):
            print("没有可选课程")
            return
        Base.show_courseinfo()
        choice_num = int(input("选择班级要关联的课程编号>>>").strip())
        course_obj_gen = Base.getinfo_from_file(courseinfo)
        for sn,obj in enumerate(course_obj_gen,1):
            if choice_num == sn:
                course = obj.name
        flag = True
        while flag:
            teacher_list = []
            print("为班级关联教师（可以关联多位教师），教师列表如下".center(50,'='))
            if not os.path.exists(teacherinfo):
                print("没有可选教师")
                return
            Base.show_teacherinfo()
            choice_te_str = input("选择班级要关联的教师编号，可以选择位教师，以空格分隔>>>").strip()
            choice_te_list = choice_te_str.split()
            for index, i in enumerate(choice_te_list):
                if i.isdigit():
                    choice_te_list[index] = int(i)
                    if index == len(choice_te_list) -1:
                        flag = False
                else:
                    print("输入编号包含非数字信息...")
                    break

            for sn,obj in enumerate(Base.getinfo_from_file(teacherinfo),1):
                if sn in choice_te_list:
                    teacher_list.append(obj.name)
            print("校区列表".center(50,'='))
            Base.show_schoolinfo()
            choice_school_num = input("选择班级所在的校区编号>>>").strip()
            if choice_school_num == '1':
                grade1 = school_bj.create_grade(name,course,teacher_list)
            elif choice_school_num == '2':
                grade1 = school_sh.create_grade(name,course,teacher_list)
            else:
                print("输入的学校编号有误")
                return
            Base.dumpinfo_to_file('grade.info',grade1)

    def create_course(self):
        print("开始创建课程".center(50,'-'))
        name = input("输入课程名：").strip()
        if os.path.exists(courseinfo):
            for obj in Base.getinfo_from_file(courseinfo):
                if obj.name == name:
                    print("\033[1;31;0m已有%s课程\033[0m"%name)
                    return
        period = input("输入课程周期（单位：月）：").strip()
        price = input("输入课程价格（单位：人民币元）：").strip()
        if name == 'python' or name == 'linux':
            school_bj.create_course(name,period,price)
        elif name == 'go':
            school_sh.create_course(name,period,price)

    def show_course_list(self):
        Base.show_courseinfo()

    def show_te_list(self):
        Base.show_teacherinfo()

    def show_grade_list(self):
        Base.show_gradeinfo()

    def show_stu_list(self):
        Base.show_studentinfo()

