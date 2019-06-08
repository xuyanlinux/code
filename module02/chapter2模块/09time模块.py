# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/24

import time
# time.time()
# time.localtime()
# time.gmtime()
# time.mktime()
# time.sleep()
# time.strftime('%Y-%m-%d')

strtime1 = '2016-05-02'
print(time.strptime(strtime1,'%Y-%m-%d'))  # 转换成一个元祖
print(time.mktime(time.strptime(strtime1,'%Y-%m-%d')))  # 转换成时间戳

timestamp = 1462118400.0
print(time.localtime(1462118400.0))
print(time.strftime('%Y-%m-%d',time.localtime(1462118400.0)))