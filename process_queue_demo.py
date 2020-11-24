import multiprocessing
import time


def w_task(q):
    '''负责写入数据至 q 队列'''
    if not q.full():
        for i in range(5):
            msg = 'data' + str(i)
            q.put(msg)
            print('%s 已进队' % msg)


def r_task(q):
    '''休息2秒等待q队列写入数据，然后输出'''
    time.sleep(2)
    while not q.empty():
        print('输出 %s' % q.get(True, 2))


if __name__ == '__main__':
    q = multiprocessing.Queue()  # 创建 q队列
    pw = multiprocessing.Process(target=w_task, args=(q,))
    pr = multiprocessing.Process(target=r_task, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
