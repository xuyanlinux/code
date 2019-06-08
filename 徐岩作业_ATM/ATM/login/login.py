# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/1


import os
from account_m import readinfo
from logs import log
logined_account = {}  # 记录已登陆的用户账号
now_account = ''  # 记录当前账号


'''
函数名称：login(func)
函数功能：用户登陆装饰器
参数说明：被装饰的函数
函数原理：1、未登录时，给出登陆提示
          2、已登陆时，直接进入相应的功能模块
          3、检测到以下几种情景，给出提示并退出登陆模块：
             用户被冻结
             密码错误
             账号不存在
          4、登陆过程调用日志模块记录日志
'''


def login(func):
    def inner(*args, **kwargs):
        global logined_account
        global now_account
        if now_account not in logined_account or logined_account[now_account] == 0:
            print("请登陆".center(50, '#'))
            user_name = input('输入用户名：').strip()
            if os.path.exists('../infodb/' + user_name):
                data = readinfo.readinfo(user_name)
                if data['status'] == 0:
                    print("用户已被冻结")
                    return
                password = input('输入密码：').strip()
                if password == data['password']:
                    print("%s 先生/女士，登录成功"%(user_name))
                    message = '%10s登陆成功！'%(user_name)
                    now_account = user_name
                    logined_account[now_account] = True
                    log.wlog('../logs/login.log', 'login', message)
                else:
                    print("密码错误")
            else:
                print("账户不存在")
        else:
            pass
        if now_account in logined_account:
            func(*args, **kwargs)
    return inner
