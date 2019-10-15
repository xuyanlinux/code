#Author:Timmy

#死锁

# from threading import Thread,Lock
# import time
#
#
# mutexA = Lock()
# mutexB = Lock()
# class Mythread(Thread):
#     def run(self):
#         self.f1()
#         self.f2()
#
#
#     def f1(self):
#         mutexA.acquire()
#         print("%s : A lock"% self.name)
#
#         mutexB.acquire()
#         print("%s : B lock"% self.name)
#         mutexB.release()
#
#         mutexA.release()
#
#     def f2(self):
#         mutexB.acquire()
#         print("%s : A lock" % self.name)
#         time.sleep(0.1)
#         mutexA.acquire()
#         print("%s : B lock" % self.name)
#         mutexA.release()
#
#         mutexB.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t = Mythread()
#         t.start()

# 用递归锁解决上面的问题
from threading import Thread,RLock
import time

mutexB = mutexA = RLock()
class Mythread(Thread):
    def run(self):
        self.f1()
        self.f2()


    def f1(self):
        mutexA.acquire()
        print("%s : A lock"% self.name)

        mutexB.acquire()
        print("%s : B lock"% self.name)
        mutexB.release()

        mutexA.release()

    def f2(self):
        mutexB.acquire()
        print("%s : B lock" % self.name)
        time.sleep(0.1)
        mutexA.acquire()
        print("%s : A lock" % self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t = Mythread()
        t.start()
