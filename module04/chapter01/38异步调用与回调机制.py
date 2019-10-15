#Author:Timmy
from concurrent.futures import ThreadPoolExecutor
import time,random
def play(name):
    print("%s is playing..."% name)
    time.sleep(random.randint(3,6))
    star = random.randint(90,100) * '*'
    return {'name':name,'star':star}

def score(inf):
    inf = inf.result()  # 这一行不能少
    name = inf['name']
    score = len(inf['star'])

    print("%s scores: %s " % (name, score))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(3)
    pool.submit(play,'xy').add_done_callback(score)
    pool.submit(play,'yy').add_done_callback(score)
    pool.submit(play,'hh').add_done_callback(score)


