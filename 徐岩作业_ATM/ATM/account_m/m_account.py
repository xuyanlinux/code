# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/1

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from account_m import writeinfo
from account_m import readinfo
from logs import log
from login import login


'''
函数名称：creat_acount()
函数功能：创建用户
参数说明：无参数
函数原理：1、检测当前用户，如果不是admin用户，提示无权限，退出
          2、如果是admin用户，根据用户的输入信息，创建新用户（输入信息为：用户名、用户密码、额度）
          3、如果用户名已存在，给出提示，退出
          4、创建过程调用日志模块记录日志
'''


@login.login
def creat_acount():
    if login.now_account == 'admin':
        account_name = input("输入要创建的账号名：").strip()
        if os.path.exists('../infodb/' + account_name):
            print("账号已存在")
            return
        account_pass = input("为新账号设置密码：").strip()
        account_amount = input("新账号的额度").strip()
        if account_amount.isdigit():
            account_amount = int(account_amount)
            data = {'name': account_name, 'password': account_pass, 'balance': account_amount, 'status': 1}
            writeinfo.writeinfo(account_name, data)
            message = '创建账号：%10s成功！' % ( account_name)
            log.wlog('../logs/login.log', 'creat_account', message)
        else:
            print("账号额度只能是数字！！！")
    else:
        print('当前账户：%s,没有创建账户的权限。' % (login.now_account))


'''
函数名称：frozen_account()
函数功能：冻结账号、解冻账号
参数说明：flag接受到的值为0，表示冻结；为1表示解冻
函数原理：1、根据传参，分析函数要实现的功能是冻结还是解冻
          2、修改目标账号的statu值为flag值
'''


@login.login
def frozen_account(flag):
    if flag == 0:
        action = '冻结'
    else:
        action = '解冻'
    if login.now_account == 'admin':
        target_account = input("输入要冻结的账户").strip()
        if os.path.exists('../infodb/' + target_account):
            data = readinfo.readinfo(target_account)
            data['status'] = flag
            writeinfo.writeinfo(target_account, data)
            message = '%s账号：%10s成功！' % (action, target_account)
            log.wlog('../logs/login.log', 'frozen_account', message)
        else:
            print("目标账号不存在")
    else:
        print('当前账户：%s,没有冻结账户的权限。' % (login.now_account))
