# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/18

flag_login = False
uname = 'tim'
passwd = '123'

def login(auth_type):
    def outer(func):
        def inner(*args,**kwargs):
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
                func(*args,**kwargs)
        return inner
    return outer


def home():
    print("---首页----")


@login('qq')
def america():
    print("----欧美专区----")

@login('wx')
def japan(str1):
    print("----日韩专区----",str1)
japan('123')