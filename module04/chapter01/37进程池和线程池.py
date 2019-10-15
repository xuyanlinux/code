#Author:Timmy

# # 进程池
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# import os,time,random
# def task(name):
#     print("%s is running: %s" % (name,os.getpid()))
#     time.sleep(random.randint(1,5))
#
#
# if __name__ == '__main__':
#     pool = ProcessPoolExecutor(5)
#     for i in range(15):
#         pool.submit(task,"xy%s"%i)
#
#     pool.shutdown(wait=True)  #默认就是True
#     print('master')


# 线程池
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import os,time,random
from threading import currentThread
def task():
    print("%s is running..." % (currentThread().getName()))
    time.sleep(random.randint(1,5))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(5)
    for i in range(15):
        pool.submit(task)

    pool.shutdown(wait=True)  #默认就是True
    print('master')
