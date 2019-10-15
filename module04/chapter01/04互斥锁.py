#Author:Timmy

# book
# 并行进程共享打印终端，会发生打印内容错乱
# from multiprocessing import Process
# import os,time
# def work():
#     print('%s is running' %os.getpid())
#     time.sleep(2)
#     print('%s is done' %os.getpid())
#
# if __name__ == '__main__':
#     for i in range(3):
#         p=Process(target=work)
#         p.start()

#book 为上面的代码加互斥锁，其实就是并发改串行，降低了效率，但避免了资源竞争
from multiprocessing import Process,Lock
import os,time

def work(lock):
    lock.acquire()  # 加锁
    print("%s is running..."%os.getpid())
    time.sleep(2)
    print("%s is done"%os.getpid())
    lock.release()  # 释放锁


if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p = Process(target=work,args=(lock,))
        p.start()