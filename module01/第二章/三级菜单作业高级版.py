#! _*_ coding:UTF-8 _*_
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
flag = True
level_record = [menu]
while flag:
    for key in level_record[-1]:print(key)
    area = input("请输入您要查询的区域（'q'退出查询，'r'返回上级菜单）：").strip()
    if area in level_record[-1]:
        level_record.append(level_record[-1][area])
        #print(level_record)
    elif area == 'q':flag = False
    elif area == 'r':
        if len(level_record) == 1:print("已经是一级菜单了！！！")
        else:
            del level_record[-1]
