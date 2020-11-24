import multiprocessing
import time


def task_p1(arg):
    for i in range(50):
        print('task_p1 进程 %s ' % arg)
        time.sleep(1)


def task_p2(arg):
    for i in range(20):
        print('task_p2 进程 %s ' % arg)
        time.sleep(0.5)


if __name__ == '__main__':
    # 创建 p1 p2 两个进程， 执行函数 target 跟名不需要加 ()， args参数为一个元组
    p1 = multiprocessing.Process(target=task_p1, args=(1,))
    p2 = multiprocessing.Process(target=task_p2, args=(2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
