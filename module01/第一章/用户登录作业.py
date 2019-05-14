#! _*_ coding:utf-8 _*_
#Author:Timmy
#创建一个列表，存储允许登录的用户名和密码
#每一个子列表中存储的，是合法的用户名和密码
user_list = [['张三','z3pass'],['李四','l4pass'],['王五','w5pass']]
count = 0

#登录控制主体
## 将用户输入的用户名和密码组合成一个列表，并判断是不是user_list的子列表
## 如果是，给出欢迎信息，跳出循环，程序结束
## 如果不是，则判断这是第几次输入错误，不足三次时，给出剩余次数；否则，给出结束提示，程序结束
while count < 3:
    username = input("输入用户名:")
    password = input("输入密码:")
    list_input = [username,password]
    if list_input in user_list:
        print("WELCOM TO MY WORLD!!!")
        break
    else:
        if count < 2:
            print("账号或密码错误，您还有%s次机会"%(2-count))
    count += 1
else:
    print("GAME OVER！！！")
