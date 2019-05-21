# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/20

import os


# def add_info(name, age, phone, dept, enroll_data):
def add_info(*args):
    offset = -50
    f = open(file='staff_table', mode='rb')
    while True:
        f.seek(offset, 2)  # seek(offset, 2)表示文件指针：从文件末尾(2)开始向前50个字符(-50)
        lines = f.readlines()  # 读取文件指针范围内所有行
        if len(lines) >= 2:  # 判断是否最后至少有两行，这样保证了最后一行是完整的
            last_line = lines[-1].decode(encoding='UTF-8')  # 取最后一行,并用utf-8编码
            break
        # 如果off为50时得到的readlines只有一行内容，那么不能保证最后一行是完整的
        # 所以off翻倍重新运行，直到readlines不止一行
        offset *= 2
    f.close()
    staff_id_last = int(last_line.strip().split(',')[0])
    staff_id_new = staff_id_last + 1
    f = open(file='staff_table', mode='a', encoding='utf-8')
    f.write('\n{0},{1},{2},{3},{4},{5}'.format(staff_id_new, args[0], args[1], args[2], args[3], args[4]))
    f.close()


def del_update(del_or_update, *args):
    lis_info_sta = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_data']
    f_r = open(file='staff_table', mode='r', encoding='utf-8')
    f_w = open(file='staff_table_del', mode='w', encoding='utf-8')

    for rline in f_r:
        if del_or_update == 'del':
            list_rline = rline.split(',')
            if list_rline[0] == str(args[0]):
                continue
            else:
                f_w.write(rline)
        elif del_or_update == 'update':
            dic_info = dict(zip(lis_info_sta, rline.split(',')))
            if dic_info[args[2]] == args[3]:
                dic_info[args[0]] = args[1]
                f_w.write(','.join(list(dic_info.values())))
            else:
                f_w.write(rline)
    f_w.close()
    f_r.close()
    os.remove('staff_table')
    os.rename('staff_table_del', 'staff_table')


def find(*args, **kwargs):
    def display():
        if args[0] == '*':
            for n in range(len(lis_info_sta)):
                if n == len(lis_info_sta) - 1:
                    print(lis_info_sta[n] + ':' + list_line[n])
                else:
                    print(lis_info_sta[n] + ':' + list_line[n], end=',')
        else:
            for key in args:
                if args.index(key) == len(args) - 1:
                    print(key + ':' + dic_info[key])
                else:
                    print(key + ':' + dic_info[key], end=',')

    f_r = open(file='staff_table', mode='r', encoding='utf-8')
    lis_info_sta = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_data']
    for line in f_r:
        line = line.strip()
        list_line = line.split(',')
        dic_info = dict(zip(lis_info_sta, list_line))
        if kwargs['compute_sign'] == 'like':
            if kwargs['condition'] in dic_info[kwargs['col']]:
                display()
            else:
                continue
        elif kwargs['compute_sign'] == '=':
            flag = dic_info[kwargs['col']] == kwargs['condition']
            if flag:
                display()
            else:
                continue
        else:
            compu_str = dic_info[kwargs['col']]+kwargs['compute_sign']+kwargs['condition']
            flag = eval(compu_str)
            if flag:
                display()
            else:
                continue
    f_r.close()


exit_flag = False


def analyze_input():
    statement = input('>>>')
    if statement.strip() == 'q' or 'Q':
        print("退出程序")
        return True
    if '>=' in statement or '<=' in statement:
        statement = statement.replace('>=', ' >= ')
        statement = statement.replace('<=', ' <= ')
    else:
        statement = statement.replace('=', ' = ')
        statement = statement.replace('>', ' > ')
        statement = statement.replace('<', ' < ')
    statement = statement.replace('  ', ' ')  # 如果符号前后原本就有空格，现在就有两个空格，把双空格换成单空格
    list_sta = statement.split(' ')
    for index, i in enumerate(list_sta):
        if index >= len(list_sta)-1:
            break
        else:
            if '"' in i and '"' in list_sta[index + 1]:
                list_sta[index] = i + ' ' + list_sta[index + 1]
                del list_sta[index + 1]
    if list_sta[0] == 'find':
        list_find = list_sta[1].split(',')
        find(*list_find, col=list_sta[5], compute_sign=list_sta[6], condition=list_sta[7].strip('"'))
    elif list_sta[0] == 'add':
        args = list_sta[2].split(',')
        add_info(*args)
    elif list_sta[0] == 'del':
        del_update('del', list_sta[-1].strip())
    elif list_sta[0] == 'update':
        del_update('update', list_sta[3], list_sta[5].strip('"'), list_sta[7], list_sta[9].strip('"'))
        # 如果没有换成单空格，最后一个参数会取空格
    else:
        print("语句错误，请重新输入")
    return False


while not exit_flag:
    exit_flag = analyze_input()