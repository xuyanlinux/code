#Author:Timmy

# book
# from multiprocessing import Process,Queue
# import time,random,os
# def consumer(q,name):
#     while True:
#         res=q.get()
#         time.sleep(random.randint(1,3))
#         print('\033[43m%s 吃 %s\033[0m' %(name,res))
#
# def producer(q,name,food):
#     for i in range(3):
#         time.sleep(random.randint(1,3))
#         res='%s%s' %(food,i)
#         q.put(res)
#         print('\033[45m%s 生产了 %s\033[0m' %(name,res))
#
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们:即厨师们
#     p1=Process(target=producer,args=(q,'egon','包子'))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,'alex'))
#
#     #开始
#     p1.start()
#     c1.start()
#     print('主')

# 解决上面例子，消费者在队列清空后，继续消费造成阻塞的问题，解决办法：
#      当生产者生产完毕后，再发一个结束信号，这样消费者在接收到结束信号后就可以break出死循环
# from multiprocessing import Process,Queue
# import time,random,os
# def consumer(q,name):
#     while True:
#         res=q.get()
#         if res is None:break
#         time.sleep(random.randint(1,3))
#         print('\033[43m%s 吃 %s\033[0m' %(name,res))
#
# def producer(q,name,food):
#     for i in range(3):
#         time.sleep(random.randint(1,3))
#         res='%s%s' %(food,i)
#         q.put(res)
#         print('\033[45m%s 生产了 %s\033[0m' %(name,res))
#
# if __name__ == '__main__':
#     q=Queue()
#     #生产者们:即厨师们
#     p1=Process(target=producer,args=(q,'egon','包子'))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,'alex'))
#
#     #开始
#     p1.start()
#     c1.start()
#
#     p1.join()
#     q.put(None)
#     print('主')

# 如果有多个生产者和消费者，按照上面的思路，有多少消费者就需要输入几次终止信号
# 新的方法
#JoinableQueue([maxsize])对象
# from multiprocessing import Process,JoinableQueue
# import time,random,os
# def consumer(q,name):
#     while True:
#         res=q.get()
#         time.sleep(random.randint(1,3))
#         print('\033[43m%s 吃 %s\033[0m' %(name,res))
#         q.task_done() #发送信号给q.join()，说明已经从队列中取走一个数据并处理完毕了
#
# def producer(q,name,food):
#     for i in range(3):
#         time.sleep(random.randint(1,3))
#         res='%s%s' %(food,i)
#         q.put(res)
#         print('\033[45m%s 生产了 %s\033[0m' %(name,res))
#     q.join() #等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束
#
# if __name__ == '__main__':
#     q=JoinableQueue() #使用JoinableQueue()
#
#     #生产者们:即厨师们
#     p1=Process(target=producer,args=(q,'egon1','包子'))
#     p2=Process(target=producer,args=(q,'egon2','骨头'))
#     p3=Process(target=producer,args=(q,'egon3','泔水'))
#
#     #消费者们:即吃货们
#     c1=Process(target=consumer,args=(q,'alex1'))
#     c2=Process(target=consumer,args=(q,'alex2'))
#     c1.daemon=True
#     c2.daemon=True
#
#     #开始
#     p1.start()
#     p2.start()
#     p3.start()
#     c1.start()
#     c2.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     #1、主进程等生产者p1、p2、p3结束
#     #2、而p1、p2、p3是在消费者把所有数据都取干净之后才会结束
#     #3、所以一旦p1、p2、p3结束了，证明消费者也没必要存在了，应该随着主进程一块死掉，因而需要将生产者们设置成守护进程
#     print('主')

# 自己写一遍
from multiprocessing import Process,JoinableQueue
import time,random,os

def consumer(name,q):
    while True:
        res = q.get()
        print("%s 吃了 %s"%(name,res))
        q.task_done()
def productor(name,food,q):
    for i in range(3):
            time.sleep(random.randint(1,3))
            res='%s%s'%(food,i)
            q.put(res)
            print('\033[45m%s 生产了 %s\033[0m' %(name,res))
    q.join() #等到消费者把自己放入队列中的所有的数据都取走之后，生产者才结束

if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=productor,args=('egon1','包子',q))
    p2 = Process(target=productor,args=('egon2','饺子',q))
    p3 = Process(target=productor,args=('egon3','混沌',q))

    c1 = Process(target=consumer,args=('alex1',q))
    c2 = Process(target=consumer,args=('alex2',q))

    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()

    print("master")

