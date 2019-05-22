# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Email: liufengjimo@live.com
# Date: 2019/5/20

import os


'''
函数名称：addinfo(*args)
函数功能：增加一条员工记录
参数调用说明： 接受的参数格式为：(name, age, phone, dept, enroll_data):
               如果添加语句是：add staff_table Mosson,18,13678789527,IT,2018-12-11，五个参数就是新条目的5个字段
实现原理：1、读取员工信息表最后一行，得到最后一行的staff_id_last值
          2、staff_id_last加一，得到新条目的staff_id值：staff_id_new
              这里读取最后一行id，采取的方式是先设置光标到倒数n行，然后读取最后n行并选择最后一行，具体请看语句注释
              这样可以避免文件过大时，直接读取文件全部内容，引起的内存浪费
          3、拼接staff_id_new和参数中的员工信息字段，得到新的条目
          4、将新条目写到文件中
'''


def add_info(*args):
    offset = -50
    # 判断手机号是否已存在，如果存在，打印信息并退出本次添加
    f_r = open(file='staff_table',mode='r',encoding='utf-8')
    for line in f_r:
        if args[2] in line:
            print("手机号已存在")
            f_r.close()
            return
    f_r.close()
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

    # 拼接新的员工信息条目，并写入文件
    f = open(file='staff_table', mode='a', encoding='utf-8')
    f.write('\n{0},{1},{2},{3},{4},{5}'.format(staff_id_new, args[0], args[1], args[2], args[3], args[4]))
    f.close()
    print("增加了1条记录！")


'''
函数名称：del_update(del_or_update, *args)
函数功能：删除或者更新条目
参数调用说明：
    1、del_or_update：接收'del'或者'update'，表示要使用的是删除功能或更新功能
    2、*args：
        如果使用更新功能：update staff_table set age=25 where name = "Alex Li"
        传入的是 ('age','25','name','Alex Li')
        如果使用删除功能：只需要传入目标条目的staff_id
实现原理：
    1、判断要实现的功能是删除，还是更新
    2、如果要实现删除功能，读取文件，找到目标条目。将目标条目之外的其他条目写入新文件。
    3、如果要实现更新功能，读取文件，找到目标条目。将每一行条目写入新的文件，其中目标
    条目写入新文件的内容，是修改后的内容
'''


def del_update(del_or_update, *args):
    lis_info_sta = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_data']
    # 打开两个文件，边读旧文件，边写新文件
    f_r = open(file='staff_table', mode='r', encoding='utf-8')
    f_w = open(file='staff_table_del', mode='w', encoding='utf-8')
    count_update = 0  # 用作更新条目的计数
    count_del = 0
    for rline in f_r:
        # 删除功能的实现
        if del_or_update == 'del':
            list_rline = rline.split(',')
            if list_rline[0] == str(args[0]):
                count_del += 1
                continue
            else:
                f_w.write(rline)
        # 更新功能的实现
        elif del_or_update == 'update':
            dic_info = dict(zip(lis_info_sta, rline.split(',')))
            # 满足两个条件，则修改条目
            # 1、信息条目符合where条件
            # 2、目标列的值不等于修改语句的目标值
            if dic_info[args[2]] == args[3] and dic_info[args[0]] != args[1]:
                dic_info[args[0]] = args[1]
                f_w.write(','.join(list(dic_info.values())))
                count_update += 1
            else:
                f_w.write(rline)
    f_w.close()
    f_r.close()
    os.remove('staff_table')
    os.rename('staff_table_del', 'staff_table')
    # 打印受执行语句影响的条目数
    if del_or_update == 'del':
        print("删除了%d条记录"%(count_del))
    else:
        print("更新了%d条记录"%(count_update))


'''
函数名称：find(*args, **kwargs)
函数功能：查询员工信息
参数调用说明：如果语句是find * from staff_table where enroll_data like "2013"
    1、args传入:   '*',就是要显示的列，'*'表示所有列，
        如果是多个但不是全别列，就传入列名，多个列名用','隔开，比如:'name','age'
    2、kwargs传入:  'enroll_data','like','2013',就是查询条件的各个字段
功能实现原理：
    1、将查询语句根据where条件分为三类：like类型、'='类型、比较类型
    2、每个类型编写自己的匹配功能
    3、读取并循环员工信息表，匹配条目后，调用display()子函数显示目标条目
'''


def find(*args, **kwargs):
    # 子函数，根据kwargs的传入参数，分为'*'和具体列名两种情景
    # 如果是'*'：输出匹配到的行的所有字段
    # 如果是具体列名：输出匹配到的行的目标列
    def display():
        if args[0] == '*':
            for n in range(len(lis_info_sta)):
                if n == len(lis_info_sta) - 1:
                    # 拼接要显示的信息，形成：“列名1：列信息，列名2：列信息”这样的字符串，比如
                    # staff_id:1,name:Alex Li,age:25,phone:13651054608,dept:Market,enroll_data:2013-04-01
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
    # 为了方便处理，将文件条目与列属性组合成字典
    lis_info_sta = ['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_data']
    count = 0
    for line in f_r:
        line = line.strip()
        list_line = line.split(',')
        dic_info = dict(zip(lis_info_sta, list_line))
        if kwargs['compute_sign'] == 'like':
            if kwargs['condition'] in dic_info[kwargs['col']]:
                display()
                count += 1
            else:
                continue
        elif kwargs['compute_sign'] == '=':
            flag = dic_info[kwargs['col']] == kwargs['condition']
            if flag:
                display()
                count += 1
            else:
                continue
        else:
            compu_str = dic_info[kwargs['col']]+kwargs['compute_sign']+kwargs['condition']
            flag = eval(compu_str)
            if flag:
                display()
                count += 1
            else:
                continue
    f_r.close()
    print("-------找到了%d条记录-----------" %(count))


exit_flag = False

'''
函数名称：
函数功能：
1、处理、分析输入语句
2、根据分析结果调用相应功能的函数
'''
def analyze_input():
    statement = input('>>>').strip()
    # 如果输入的是'q'或'Q'，打印信息并退出程序
    if statement == 'q' or statement == 'Q':
        print("退出程序")
        return True
    # 因为我使用空格对执行语句进行切割，所以需要在=、>、<等字符前后加上空格
    # 也考虑用户输入时本来就有空格，那么还需要将双空格再改为单空格
    if '>=' in statement or '<=' in statement:
        statement = statement.replace('>=', ' >= ')
        statement = statement.replace('<=', ' <= ')
    else:
        statement = statement.replace('=', ' = ')
        statement = statement.replace('>', ' > ')
        statement = statement.replace('<', ' < ')
    statement = statement.replace('  ', ' ')  # 如果符号前后原本就有空格，现在就有两个空格，把双空格换成单空格
    # 将输入语句转换成列表，方便提取字段
    list_sta = statement.split(' ')
    # 输入语句如果是这样：update staff_table set age=25 where name = "Alex Li"
    # 需要将"Alex Li"作为列表的一个元素，但上面字符串转换列表是用空格作为分割符，所以需要以下处理
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

# 循环调用函数，直到输入结束指令'q'或者'Q'
while not exit_flag:
    exit_flag = analyze_input()