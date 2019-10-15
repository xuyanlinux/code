#! _*_ coding:utf-8 _*_
from cls_def import *
import pickle
import sys
import os

def login():
    name = input('username : ')
    passwd = input('password : ')
    for s in Base.getinfo_from_file(userinfo):
        usr, pwd, identify = s.strip().split('|')
        if usr == name and passwd == pwd:
            return {'result': True, 'name': name, 'id': identify}
    return {'result': False, 'name': name}


def role_act():
    ret = login()
    if ret['result']:
        print('\033[1;32;40m登录成功\033[0m')
        print(ret['id']+'info')
        for obj in Base.getinfo_from_file(ret['id']+'.info'):
            if obj.name == ret['name']:
                obj.menu()
    else:
        print('登录失败')


'''
函数名称：creat_admin()
函数功能：创建超级管理账号admin
形参说明：无
返回值  ：无

'''
def create_admin():
    if os.path.exists(userinfo):
        for obj in Base.getinfo_from_file(userinfo):
            if 'admin' == obj.split('|')[0]:
                break
        else:
            admin_info = 'admin'+'|'+admin_passwd+'|'+'manager'
            Base.dumpinfo_to_file(userinfo,admin_info)
    else:
        admin_info = 'admin' + '|' + admin_passwd + '|' + 'manager'
        Base.dumpinfo_to_file(userinfo, admin_info)
    if os.path.exists(managerinfo):
        for obj in Base.getinfo_from_file(managerinfo):
            if 'admin' == obj.name:
                break
        else:
            admin = Manager('admin',30,'M')
            Base.dumpinfo_to_file(managerinfo,admin)
    else:
        admin = Manager('admin', 30, 'M')
        Base.dumpinfo_to_file(managerinfo, admin)

def main():

    create_admin()
    while True:
        title = "选课系统gogogo".center(50,'#')
        print("\033[1;32;40m%s\033[0m"%title)
        action_list = ['注册','登录']
        for index,act in enumerate(action_list,1):
            print(index,act)
        act = input("选择操作编号，输入q|Q可以退出程序>>>").strip()
        if act.upper() == 'Q':
            break
        elif act.isdigit():
            act = int(act)
            if act == 1:
                Studente.sign()
            elif act == 2:
                role_act()
            else:
                print("输入的编号错误...")
        else:
            print("输入必须是操作对应的编号！")

main()
