#Author:Timmy

#一个子进程
#book
# from multiprocessing import Process
# import time
# import random
# import os
#
# def task():
#     print('%s is piaoing' %os.getpid())
#     time.sleep(random.randrange(1,3))
#     print('%s is piao end' %os.getpid())
#
# if __name__ == '__main__':
#     p=Process(target=task)
#     p.start()
#     p.join() #等待p停止,才执行下一行代码
#     print('主')

# 多个子进程

from multiprocessing import Process
import time
import random
import os

def task(name):
    print("%s is piaoing"%os.getpid())
    # print("%s is piaoing"%name)
    time.sleep(random.randrange(1,3))
    print("%s is piaoend"%os.getpid())
    # print("%s is piaoend"%name)

# if __name__ == '__main__':
#     p1 = Process(target=task,args=('liu',))
#     p2 = Process(target=task,args=('zhang',))
#     p3 = Process(target=task,args=('guo',))
#     p4 = Process(target=task,args=('wang',))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     p4.join()
#
#     print("master")


# book 练习题
#保证最先输出-------->4
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('-------->4')

# 效果二：保证最后输出-------->4
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     print('-------->4')

# #效果三：保证按顺序输出 1 2 3 4
# from multiprocessing import Process
# import time
# import random
#
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p1.join()
#     p2.start()
#     p2.join()
#     p3.start()
#     p3.join()
#     print('-------->4')

#那种属于并发，那种属于串行？

# 1、2属于并发；3属于串行