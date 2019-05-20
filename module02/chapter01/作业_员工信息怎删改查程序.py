# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/20

import os
def add_info(name,age,phone,dept,enroll_date):
    count = 0
    pho_flag = True
    f_r = open(file='staff_table', mode='r', encoding='utf-8')
    for line in f_r:
        if phone in line:
            pho_flag = False
            f_r.close()
            print("手机号码已存在！")
            return
        else:
            count += 1
    f_r.close()
    id = count + 1
    f = open(file='staff_table',mode='a',encoding='utf-8')
    f.write('\n{0},{1},{2},{3},{4},{5}'.format(id,name,age,phone,dept,enroll_date))
    f.close()


def del_info(id):
    f_r = open(file='staff_table',mode='r',encoding='utf-8')
    lines = f_r.readlines()
    f_r.close()

    f_w = open(file='staff_table',mode='w',encoding='utf-8')
    for line in lines:
        if id in line:
            continue
        f_w.write(line)
    f_w.close()


def update_info(key_tar,new_value,key_refer,refer_value):
    lis_info_sta = ['id','name','age','phone','dept','enroll_date']
    f_r = open(file='staff_table',mode='r',encoding='utf-8')
    f_w = open(file='staff_table_new',mode='w',encoding='utf-8')
    for line in f_r:
        dic_info = dict(zip(lis_info_sta,line.split(',')))
        if dic_info[key_refer] == refer_value:
            dic_info[key_tar] = new_value
            f_w.write(','.join(list(dic_info.values())))
        else:
            f_w.write(line)
    f_w.close()
    f_r.close()
    os.remove('staff_table')
    os.rename('staff_table_new','staff_table')


def find(*args,**kwargs):
    f_r = open(file='staff_table', mode='r', encoding='utf-8')
    lis_info_sta = ['id', 'name', 'age', 'phone', 'dept', 'enroll_date']
    for line in f_r:
        dic_info = dict(zip(lis_info_sta, line.split(',')))
        if kwargs['compute_sign'] == 'like':
            if kwargs['condition'] in dic_info[kwargs['col']]:
                if args[0] == '*':
                    print(line)
                for key in args:
                    if lis_info_sta.index(key) == len(lis_info_sta) - 1:
                        print(dic_info[key])
                    else:
                        print(dic_info[key], end=',')
            else:
                continue
        else:
            compu_str = dic_info[kwargs['col']]+kwargs['compute_sign']+kwargs['condition']
            flag = eval(compu_str)
            if flag:
                if args[0] == '*':
                    print(line.strip())
                    continue
                for key in args:
                    if lis_info_sta.index(key) == len(lis_info_sta) - 1:
                        print(dic_info[key])
                    else:
                        print(dic_info[key], end=',')
            else:
                continue
    f_r.close()



find('*',col='age',compute_sign='>',condition = '22')
# find('name',col= 'age',compute_sign='>',condition = '22')


# add_info('xuyan','30','1888888','engner','20190202')
# update_info('dept','IT','dept','Market')
