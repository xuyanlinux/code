# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/1
import json

'''
函数名称：writeinfo(account,data)
函数功能：修改目标账号的信息
参数说明：account，目标账号
          data，新的账号信息
函数原理：1、json序列化写入新的账号信息
'''
def writeinfo(account,data):
    f = open(file='../infodb/'+account,mode='w',encoding='utf-8')
    json.dump(data,f, sort_keys=True, indent=4, separators=(',', ': '))
    f.close()


