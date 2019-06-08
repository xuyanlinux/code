# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/2

import os
import sys
import time
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from account_m import m_account
from cash_m import m_cash
from shopping import shopping
from login import login

menu = ['购物','提现','转账','还款','新建账户','冻结账户','解冻账户']


'''
函数名称：main()
函数功能：程序入口，根据用户选择，调用各种功能函数
参数说明：无参数
函数原理：1、打印功能菜单
          2、根据用户选择，调用相关功能的函数
          3、转账功能比较特殊，目标账号是否存在的判断放到了main函数中
          4、输入'q'可退出程序，如果进入了购物模块，第一次输入'q'时退出购物，第二次输入退出整个程序
'''

@login.login
def main():
    while True:
        time.sleep(0.5)
        print("操作选项".center(50, '*'))
        for index,action in enumerate(menu):
            print(index,action)
        service = input('选择你需要的服务编号,或输入q结束操作>>>').strip()
        if service == 'q':
            break
        elif service.isdigit():
            num = int(service)
            if num < 0 or num > len(menu) - 1:
                print("请输入正确的服务编号！")
            elif num == 0:
                shopping.shopping()
            elif num == 1:
                m_cash.withdraw()
            elif num ==2:
                tar_account = input("输入转账的目标账号：").strip()
                if os.path.exists('../infodb/' + tar_account):
                    m_cash.repay(tar_account)
                else:
                    print("目标账号不存在")
            elif num == 3:
                m_cash.repay()
            elif num ==4:
                m_account.creat_acount()
            elif num == 5:
                m_account.frozen_account(0)
            elif num == 6:
                m_account.frozen_account(1)
        else:
            print('请输入输入数字编号！')


main()

