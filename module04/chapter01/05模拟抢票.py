#Author:Timmy

#book
#问题：只有一张票，但显示10个人都买到票了，最后文件中票数为0，搞笑么？至少了一张票，但却显示10个人都有票
# from multiprocessing import Process
# import time,json
#
# def search(name):
#     dic=json.load(open('db.txt'))
#     time.sleep(1)
#     print('\033[43m%s 查到剩余票数%s\033[0m' %(name,dic['count']))
#
# def get(name):
#     dic=json.load(open('db.txt'))
#     time.sleep(1) #模拟读数据的网络延迟
#     if dic['count'] >0:
#         dic['count']-=1
#         time.sleep(1) #模拟写数据的网络延迟
#         json.dump(dic,open('db.txt','w'))
#         print('\033[46m%s 购票成功\033[0m' %name)
#
# def task(name):
#     search(name)
#     get(name)
#
# if __name__ == '__main__':
#     for i in range(10): #模拟并发10个客户端抢票
#         name='<路人%s>' %i
#         p=Process(target=task,args=(name,))
#         p.start()

#book  解决上面的问题
# from multiprocessing import Process,Lock
# import time,json
#
# def search(name):
#     # lock.acquire()
#     dic=json.load(open('db.txt'))
#     time.sleep(1)
#     print('\033[43m%s 查到剩余票数%s\033[0m' %(name,dic['count']))
#     # lock.release()
#
# def get(name):
#     # lock.acquire()
#     dic=json.load(open('db.txt'))
#     time.sleep(1) #模拟读数据的网络延迟
#     if dic['count'] >0:
#         dic['count']-=1
#         time.sleep(1) #模拟写数据的网络延迟
#         json.dump(dic,open('db.txt','w'))
#         print('\033[46m%s 购票成功\033[0m' %name)
#     else:
#         print('\033[45m%s 没有票了\033[0m' %name)
#     # lock.release()
#
# def task(name,lock):
#     lock.acquire()
#     search(name)
#     get(name)
#     lock.release()
# if __name__ == '__main__':
#     lock = Lock()
#     for i in range(10): #模拟并发10个客户端抢票
#         name='<路人%s>' %i
#         p=Process(target=task,args=(name,lock,))
#         p.start()


# book上的解答,与我自己的不同如下
# 1、使用with lock的写法
# 2、查票不加锁，抢票加锁，更模拟过程更逼真
from multiprocessing import Process,Lock
import time,json

def search(name):
    # lock.acquire()
    dic=json.load(open('db.txt'))
    time.sleep(1)
    print('\033[43m%s 查到剩余票数%s\033[0m' %(name,dic['count']))
    # lock.release()

def get(name):
    # lock.acquire()
    dic=json.load(open('db.txt'))
    time.sleep(1) #模拟读数据的网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(1) #模拟写数据的网络延迟
        json.dump(dic,open('db.txt','w'))
        print('\033[46m%s 购票成功\033[0m' %name)
    else:
        print('\033[45m%s 没有票了\033[0m' %name)
    # lock.release()

def task(name,lock):
    search(name)
    with lock:
        get(name)
if __name__ == '__main__':
    lock = Lock()
    for i in range(10): #模拟并发10个客户端抢票
        name='<路人%s>' %i
        p=Process(target=task,args=(name,lock,))
        p.start()
