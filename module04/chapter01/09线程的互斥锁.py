#Author:Timmy
from threading import Thread
import time

n = 100
def task():
    global n
    num = n
    time.sleep(0.1)
    n = num - 1


if __name__ == '__main__':
    t_l = []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
    print(len(t_l))
    for t in t_l:
        t.join()
    print('主',n)


# from threading import Thread,Lock
# import time
#
# n = 100
# def task(lock):
#     global n
#     lock.acquire()
#     num = n
#     time.sleep(0.1)
#     n = num - 1
#     lock.release()
#
# if __name__ == '__main__':
#     lock = Lock()
#     t_l = []
#     for i in range(100):
#         t = Thread(target=task,args=(lock,))
#         t_l.append(t)
#         t.start()
#
#     for t in t_l:
#         t.join()
#     print('主',n)
