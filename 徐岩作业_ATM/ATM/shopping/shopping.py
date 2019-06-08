#! _*_ coding:utf-8 _*_
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from cash_m import m_cash
from login import login
##商品列表
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

@login.login
def shopping():
    print("商品列表".center(50, '#'))
    print("编号", "名称".center(10), "价格".center(6))
    count = 0    ## 定义变量count，用来存储、打印编号，我觉得对这个需求来说，count计数比用index简单
    for product in goods:
        print(count, product['name'].center(15), product['price'])
        count += 1
    shopping_cart = [] ## 这个列表就是购物车，用于存储用户选择的商品

 ##购物车主体程序：
        # 1. 允许用户根据商品编号购买商品
        # 2. 用户选择商品后，检测余额是否够，够就将商品加入购物车直接扣款，不够就提醒
        # 3. 键入'q'可以退出程序，退出前打印已购买商品和余额
        # 4. 高亮显示关键输出，如余额，商品已加入购物车等消息
    while True:
        choice = input("请输入您要买的商品编号,输入'q'结算退出：").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice < 0 or choice >= len(goods):
                print("正确的编号范围是：%s-------%s" % (0, len(goods) - 1))
            else:
                m_cash.consume(goods[choice]['price'])
                shopping_cart.append(goods[choice])
                print("\033[1;36m%s\033[0m已加入购物车！" % (goods[choice]['name']))
        elif choice == 'q':
            if len(shopping_cart) > 0:
                print('\033[1;34m您购买的产品清单如下：\033[0m')
                for product in shopping_cart:
                    print('\033[1;32m%s\033[0m'%(product['name']))
            else:
                print("您未选择任何商品！")
            break
        else:
            print("请输入有效的商品编号，或输入'q'结算退出。")