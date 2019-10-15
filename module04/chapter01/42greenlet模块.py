#Author:Timmy

# pip install greenlet
from greenlet import greenlet

def eat(name):
    print("%s is eat 1"%name)
    gr2.switch('egon')
    print("%s is eat 2..."%name)
    gr2.switch()

def play(name):
    print("%s is play 1"% name)
    gr1.switch()
    print("%s is play 2"% name)

if __name__ == '__main__':
    gr1 = greenlet(eat)
    gr2 = greenlet(play)
    gr1.switch('egon')