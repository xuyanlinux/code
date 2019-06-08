# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/24

import datetime

# d = datetime.datetime.now()
# print(d)
# print(d.timestamp())
# print(d.today())
# print(d.year)
# print(d.timetuple())

# 把一个时间戳转为datetime日期类型
# d2 = datetime.date.fromtimestamp(322222)
# print(d2)

# 时间运算
# d3 = datetime.datetime.now()
# print(d3)
# print(datetime.datetime(2017, 10, 1, 12, 53, 11, 821218))
#
# print(d3 + datetime.timedelta(4))  # 当前时间+4天
#
# print(d3 + datetime.timedelta(hours=4))  # 当前时间加s4小时

# 时间替换
d4 = datetime.datetime.now()
print(d4.replace(year=2016))
