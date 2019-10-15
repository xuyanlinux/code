#Author:Timmy

#简单实例
# from threading import Timer
#
#
# def task(name):
#     print("hello, %s" % name)
#
# if __name__ == '__main__':
#     t = Timer(5,function=task,args=('xy',))
#     t.start()

# 模拟验证码

from threading import Timer
import random

class Verify:
    def __init__(self):
        self.cache()

    def cache(self, interval = 5):
        self.verti_code = self.pro()
        print(self.verti_code)

        self.t = Timer(interval,function=self.cache)
        self.t.start()

    def pro(self, n = 3):
        str_v = ''
        for n in range(n):
            st1 = str(random.randint(0,9))
            st2 = chr(random.randint(65,90))
            str1 = random.choice([st1,st2])
            str_v += str1
        return str_v

    def check(self):
        while True:
            password = input(">>>").strip()
            if password == self.verti_code:
                print("u got it")
                self.t.cancel()
                break


ver = Verify()
ver.check()