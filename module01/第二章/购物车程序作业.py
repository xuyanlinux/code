#! _*_ coding:utf-8 _*_

##商品列表
goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}
]

##使用一个字典存储用户名和密码，需要多个用户时，只需追加键值对
user_info = {'tim':'123'}

##让用户输入用户名
username = input("请输入用户名：")
password = input(("请输入密码："))

##用户名、密码正确，进入购物程序
if user_info.get(username) == password:

##请用户输入工资，然后打印商品列表
    balance = int(input("请输入你的工资："))
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
                if goods[choice]['price'] <= balance:
                    shopping_cart.append(goods[choice])
                    balance -= goods[choice]['price']
                    print("\033[1;36m%s\033[0m已加入购物车！" % (goods[choice]['name']))
                else:
                    print("您的余额为：%s,不够了" % (balance))
        elif choice == 'q':
            if len(shopping_cart) > 0:
                print('\033[1;34m您购买的产品清单如下：\033[0m')
                for product in shopping_cart:
                    print('\033[1;32m%s\033[0m'%(product['name']))
            else:
                print("您未选择任何商品！")
            print('您的余额：\033[1;31m%s\033[0m'%(balance))
            break
        else:
            print("请输入有效的商品编号，或输入'q'结算退出。")

##用户名、密码错误，给出提示，结束程序
else:
    print("用户名或密码有误！")

