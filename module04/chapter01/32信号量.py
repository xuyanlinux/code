#Author:Timmy

from threading import Thread,Semaphore,current_thread
import time,random

sem = Semaphore(3)

def task():
    sem.acquire()
    print("%s running..." % current_thread().getName())
    time.sleep(random.randint(3,5))
    sem.release()

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=task,)
        t.start()