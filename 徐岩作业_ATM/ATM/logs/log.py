# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/6/1

import logging

'''
函数名称：函数名称：wlog(log_file,funcname,message)
函数功能：写日志，将日志同步写到标准输出，和日志文件
参数说明：logfile：目标日志文件，账号登陆、创建、冻结等相关操作写入login.log
                                 账户金额相关操作消费、还款、转账等写入consume.log
          funcname:调用日志模块的函数名
          message：日志信息
函数原理：1、根据日志模块的常规操作方法，记录相关函数传递过来的信息
          2、一个需要注意的地方：每次调用完后，及时清除handler，避免重复打印
'''

def wlog(log_file,funcname,message):

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # file handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.INFO)

    # formatter
    formatter = logging.Formatter('%(asctime)s - %(name)15s - %(levelname)s - %(message)s')
    # bind formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger = logging.getLogger(funcname)
    logger.handlers.clear()  # 调用完成后，清理handlers，避免重复打印（第几次调用，就会打印几条重复日志）
    logger.setLevel(logging.INFO)  # logger 优先级高于其它输出途径的

    # add handler   to logger instance
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info(message)


