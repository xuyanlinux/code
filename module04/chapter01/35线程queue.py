#Author:Timmy
import queue

q = queue.Queue(3)
q.put('first')
q.put(2)
q.put('third')

#q.put(4)
# q.put(4,block=False)  # == q.put_nowait(4)
# q.put_nowait(4)
# q.put(4,block=True,timeout=3)
print(q.get())
print(q.get())
print(q.get())
# print(q.get())
print(q.get(block=False)) # == q.get_nowait()


queue.LifoQueue()
queue.PriorityQueue()