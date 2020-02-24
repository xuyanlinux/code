#Author:Timmy

import pymysql

username = input('用户名>>>').strip()
password = input('密码>>>').strip()

#连接
conn = pymysql.connect(
    host = '10.0.0.101',
    user = 'root',
    port = 3306,
    password = '123',
    database = 'db41',
    charset = 'utf8'
)

# 游标
cursor = conn.cursor()
#cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行sql语句
sql = 'select * from userinfo where name = "%s" and pwd = "%s" '% (username, password)
print(sql)
res = cursor.execute(sql)
print(res)

cursor.close()
conn.close()


if res:
    print("登录成功")
else:
    print("用户名或密码错误")