#Author:Timmy
#写一个三次认证
##功能：实现用户输入用户名和密码，当用户名为seven或alex且密码为123
##时。显示登录成功，否则登录失败，失败时允许重复输入三次


user_info = {'seven':'123','alex':'123'}
count = 2
while count >= 0:
    username = input('请输入用户名：>>>').strip()
    password = input('请输入密码：>>>').strip()
    if user_info.get(username) == None:
        if count == 0:
            print('三次登录失败，over！')
        else:
            print("用户名或密码错误，您还有%s次机会！"%(count))
        count -= 1
    else:
        print('登录成功！')
        break