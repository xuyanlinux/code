# Author:Timmy

# 方式1
# from threading import Thread
# import time
#
# def eat(name):
#     print("%s is eatting"%name)
#     time.sleep(1)
#     print("%s chiwanle "%name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=eat,args=('xy',))
#     t.start()
#     print("主线程")

# 方式二

from threading import Thread
import time


class Mythread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("%s is eatting..." % self.name)
        time.sleep(1)
        print("%s chiwanle" % self.name)


if __name__ == '__main__':
    t = Mythread('xy')
    t.start()
    print("主线程")
