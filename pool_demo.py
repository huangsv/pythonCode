import multiprocessing
import time, os


def task(arg):
    print('进程(%s)输出 %s' % (os.getpid(), arg))
    print('--------------------')
    time.sleep(1)


if __name__ == '__main__':
    # 创建 三个 进程工作区
    p = multiprocessing.Pool(3)
    # 由于三个进程工作区去完成 30 个任务
    for i in range(30):
        p.apply_async(task, args=(i,))
    p.close()
    p.join()
