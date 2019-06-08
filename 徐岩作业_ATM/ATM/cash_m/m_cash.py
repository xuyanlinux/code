# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/1

from account_m import readinfo
from account_m import writeinfo
from logs import log
from login import login


'''
函数名称：consume(spend,*args)
函数功能：消费或转账（转出账号操作）
参数说明：如果是消费，无需为args传参；如果要转账，args接收值为目标账号，作为记录日志的信息点
函数原理：1、根据参数，判断要实现的功能是消费还是转账
          2、如果是消费，打印当前账号的余额和应还金额，然后根据用户的消费金额修改账号信息
          3、如果是转账，根据转账金额修改账号信息
          4、消费或转账过程中，调用日志模块进行记录
          5、金额不足时给出提示
'''
@login.login
def consume(spend,*args):
    if len(args) > 0:
        action = '转账给 %s'%(args[0])
    else:
        action = '消费'
    data = readinfo.readinfo(login.now_account)
    if spend <= data['balance']:
        data['balance'] = data['balance'] - spend
        writeinfo.writeinfo(login.now_account, data)
        message = "-----%s------%s金额:%10s ，余额：%10s"%(login.now_account,action,spend,data['balance'])
        log.wlog('../logs/consume.log','consume',message)
    else:
        print("余额不足")



'''
函数名称：repay(*args)
函数功能：还款或转账（转入账号操作）
参数说明：如果要还款，无需传参；如果要转账，传参为目标账号
函数原理：1、根据参数，判断要实现的功能是还款还是转账
          2、如果是还款，打印当前账号的余额和应还金额，然后根据用户的还款额修改账户信息
          3、如果是转账，打印目标账号的余额和应还金额，然后根据用户的转账金额修改转入账号的信息，并调用consume
             函数修改转出账号的信息
          4、还款或转账过程中，调用日志模块进行记录
          5、这里设定每个账号的额度是15000，如果还款或转账金额超出找好额度，给出提示
'''
@login.login
def repay(*args):
    if len(args) > 0:
        account = args[0]
        action = '转账'
        action_mes = '收到%s转账'%(login.now_account)
    else:
        account = login.now_account
        action = '还款'
        action_mes = '还款'
    data = readinfo.readinfo(account)
    print("%10s余额："%(account), data['balance'])
    print("%10s应还："%(account),15000-data['balance'])
    repay_value = input("输入%s的金额："%(action)).strip()
    if repay_value.isdigit():
        repay_value = int(repay_value)
        if repay_value > 0 and repay_value <= 15000-data['balance']:
            if len(args) > 0:
                consume(repay_value,account)
            data['balance'] +=  repay_value
            writeinfo.writeinfo(account,data)
            message = "-----%s------%s金额:%10s ，余额：%10s" % (account, action_mes,repay_value,data['balance'])
            log.wlog('../logs/consume.log', 'repay', message)
        elif repay_value > 15000 - data['balance']:
            print("还款数额超出目标账户的额度")
        else:
            print("还款必须是正数！！！！")
    else:
        print("还款金额必须是数字！！")


'''
函数名称：withdraw()
函数功能：提现
参数说明：无参数
函数原理：1、根据提现金额，计算手续费
          2、从账号余额扣除提现金额和手续费
          3、金额不足时出提示信息
          4、提现过程中调用日志模块记录日志
'''
@login.login
def withdraw():
    data = readinfo.readinfo(login.now_account)
    print("余额：", data['balance'])
    withdraw_va = input("输入要取现的数额：").strip()
    if withdraw_va.isdigit():
        withdraw_va = int(withdraw_va)
        service_charge = withdraw_va * 0.05
        total = withdraw_va + service_charge
        if total <= data['balance']:
            data['balance'] -=  total
            writeinfo.writeinfo(login.now_account,data)
            message = "-----%s------取现金额:%10s，手续费：%10s，余额：%10s" % (login.now_account, withdraw_va, service_charge,data['balance'])
            log.wlog('../logs/consume.log', 'withdraw', message)
        else:
            print("取现额度超出余额！！！")
    else:
        print("取现金额必须是数字！！")