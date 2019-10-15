#Author:Timmy
import gevent
from gevent import monkey;monkey.patch_all()
import time

monkey.patch_all()
def eat(name):
    print("%s is eat 1"%name)
    # gevent.sleep(3)
    time.sleep(5)
    print("%s is eat 2..."%name)


def play(name):
    print("%s is play 1"% name)
    # gevent.sleep(4)
    time.sleep(4)
    print("%s is play 2"% name)

if __name__ == '__main__':

    star_time = time.time()
    g1 = gevent.spawn(eat,'egon')
    g2 = gevent.spawn(play,'egon')

    # g1.join()
    # g2.join()
    gevent.joinall([g1,g2])  #  取代上面两行
    stop_time = time.time()
    print(stop_time - star_time)
    print('master')