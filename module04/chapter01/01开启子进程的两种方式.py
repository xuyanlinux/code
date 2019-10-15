#Author:Timmy
#方式一
# from multiprocessing import Process
# import time
#
# def task(name):
#     print("%s is running..."%name)
#     time.sleep(3)
#     print("%s is done."%name)
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=("进程1", ))  # 这里必须有逗号
#     p.start()  # 这个语句只是给操作系统发了一个开启子进程的信号
#     print("主进程...")

# book
# from multiprocessing import Process
# import time
#
# def piao(name):
#     print("%s piaoing"%name)
#     time.sleep(1)
#     print("%s piao wan le "%name)
#
# if __name__ == '__main__':
#     p1 = Process(target=piao,args=('liu',))
#     p2 = Process(target=piao,args=('zhang',))
#     p3 = Process(target=piao,args=('guo',))
#     p4 = Process(target=piao,args=('wang',))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     print("master ")





#方式2
from multiprocessing import Process
import time


class Myprocess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s is running..."%self.name)
        time.sleep(3)
        print("%s is done"%self.name)

if __name__ == '__main__':
    p = Myprocess("子进程1")
    p.start()
    print(p.is_alive())
    time.sleep(4)
    print(p.is_alive())
    print(p.pid)
    print("主进程")

#book
# from multiprocessing import Process
# import time
#
# class Piao(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#
#     def run(self):
#         print("%s piaoing..."%self.name)
#         time.sleep(1)
#         print("%s piao wan le "%self.name)
#
# if __name__ == '__main__':
#     p1 = Piao('liu')
#     p2 = Piao('zhang')
#     p3 = Piao('guo')
#     p4 = Piao('wang')
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p4.start()
#
#     print("master")



#子进程和主进程内存是否共享
# from multiprocessing import Process
# import time
# n=100 #在windows系统中应该把全局变量定义在if __name__ == '__main__'之上就可以了

# def work():
#     global n
#     n=0
#     print('子进程内: ',n)
#
#
# if __name__ == '__main__':
#     p=Process(target=work)
#     p.start()
#     print('主进程内: ',n)
#
#     time.sleep(1)
#     print('主进程内：',n)