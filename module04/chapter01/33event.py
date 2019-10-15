#Author:Timmy

from threading import Thread,Event,current_thread
import time
ev = Event()
def student():
    print("%s is studing..."% current_thread().getName())
    ev.wait()
    print("%s is playing..." % current_thread().getName())

def teacher():
    print("老师在上课...")
    time.sleep(5)
    ev.set()

if __name__ == '__main__':
    for i in range(3):
        st = Thread(target=student,name='sno'+str(i))
        st.start()
    te = Thread(target=teacher)
    te.start()