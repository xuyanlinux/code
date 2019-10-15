#Author:Timmy
from multiprocessing import Process,Queue

q=Queue(3)

#put ,get ,put_nowait,get_nowait,full,empty
q.put(1)
q.put(2)
q.put(3)
print(q.full()) #满了
#q.put(4) #再放就阻塞住了,队列中有内容被取走以后才能继续put

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了
#print(q.get()) #再取就阻塞住了，等到队列中有内容了才能继续取