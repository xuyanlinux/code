#_*_coding:utf-8_*_
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
# flag = True
# while flag:
#     province = input(">>>请输入您要查询的省，输入'q'可以退出查询：")
#     if province in menu:
#         print("一级菜单：%s".center(50,'#') % (province))
#         for key in menu[province]:print(key)
#         while flag:
#             city = input(">>>请输入您要查询的市，输入'q'可以退出查询，输入'e'可以返回上级菜单：")
#             if city in menu[province]:
#                 print("二级菜单：%s----->%s".center(50,'#')%(province,city))
#                 for key in menu[province][city]: print(key)
#                 while flag:
#                     community = input(">>>请输入您要查询的社区，输入'q'可以退出查询，输入'e'可以返回上级菜单：")
#                     if community in menu[province][city]:
#                         print("三级菜单：%s----->%s----->%s".center(50,'#') % (province, city,community))
#                         for key in menu[province][city][community]:
#                             print(key)
#                     elif community == 'q':
#                         flag = False
#                     elif community == 'e':
#                         break
#             elif city == 'q':
#                 flag = False
#             elif city == 'e':
#                 break
#     elif province == 'q':
#         flag = False

flag = True
while flag:
    province = input(">>>请输入您要查询的省，输入'q'可以退出查询：")
    if province in menu:
        while flag:
            print("一级菜单：%s".center(50,'#') % (province))
            for key in menu[province]:print(key)
            city = input(">>>请输入您要查询的市，输入'q'可以退出查询，输入'e'可以返回上级菜单：")
            if city in menu[province]:
                while flag:
                    print("二级菜单：%s----->%s".center(50,'#')%(province,city))
                    for key in menu[province][city]: print(key)
                    while flag:
                        community = input(">>>请输入您要查询的社区，输入'q'可以退出查询，输入'e'可以返回上级菜单：")
                        if community in menu[province][city]:
                            print("三级菜单：%s----->%s----->%s".center(50,'#') % (province, city,community))
                            for key in menu[province][city][community]:
                                print(key)
                            continue
                        elif community == 'q':
                            flag = False
                        elif community == 'e':
                            break
            elif city == 'q':
                flag = False
            elif city == 'e':
                break
    elif province == 'q':
        flag = False