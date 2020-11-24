import gevent
from gevent.lock import Semaphore


def task1():
    for i in range(5):
        sem.acquire()
        print('task1, this is ', i)
        sem.release()
        gevent.sleep(0.5)


def task2():
    for i in range(5):
        sem.acquire()
        print('task2, that is ', i)
        sem.release()
        gevent.sleep(0.3)


if __name__ == '__main__':
    sem = Semaphore(1)
    g1 = gevent.spawn(task1)
    g2 = gevent.spawn(task2)
    gevent.joinall([g1, g2])
