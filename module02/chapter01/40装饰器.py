# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/18
flag_login = False
uname = 'aaa'
passwd = '123'

def login(func):
    def inner():
        global flag_login
        if flag_login == False:
            user_name = input('输入用户名：')
            password = input('输入密码：')
            if user_name == uname and password == passwd:
                print('Welcome to my house!')
                flag_login = True
            else:
                print('用户名或密码有误！')
        else:
            print('您已登陆')
        if flag_login == True:
            func()
    return inner


def home():
    print("---首页----")


@login
def america():
    # login()
    print("----欧美专区----")


@login
def japan():
    # login()
    print("----日韩专区----")


# def login():
#     global flag_login
#     if flag_login == False:
#         user_name = input('输入用户名：')
#         password = input('输入密码：')
#         if user_name == uname and password == passwd:
#             print('Welcome to my house!')
#             flag_login = True
#         else:
#             print('用户名或密码有误！')
#     else:
#         print('您已登陆')




# japan = login(japan)
japan()

# america = login(america)
america()

