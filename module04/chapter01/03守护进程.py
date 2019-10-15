#Author:Timmy

#book
# from multiprocessing import Process
# import time
# import random
#
# def task(name):
#     print('%s is piaoing' %name)
#     time.sleep(random.randrange(1,3))
#     print('%s is piao end' %name)
#
#
# if __name__ == '__main__':
#     p=Process(target=task,args=('egon',))
#     p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
#     p.start()
#     print('主') #只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了

#book练习题
#思考下列代码的执行结果有可能有哪些情况？为什么？

from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Process(target=foo)
    p2=Process(target=bar)

    p1.daemon=True
    p1.start()
    time.sleep(1)
    p2.start()
    print("main-------")