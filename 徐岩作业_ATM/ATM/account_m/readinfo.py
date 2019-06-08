# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/1
import json

'''
函数名称：readinfo(account)
函数功能：读取并返回目标账号的信息
参数说明：account，目标账号
函数原理：1、json序列化读取账号信息
          2、返回账号信息
'''


def readinfo(account):
    f = open(file='../infodb/'+account, mode='r', encoding='utf-8')
    data = json.load(f)
    f.closed
    return data