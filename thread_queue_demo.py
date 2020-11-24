import threading, time
import queue


class ThreadWrite(threading.Thread):
    '''这个进行负责写入数据'''
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.data = queue

    def run(self):
        for i in range(5):
            msg = 'data' + str(i)
            self.data.put(msg)
            print('%s write %s' % (self.getName(), msg))
            time.sleep(1)  # 等待 读取 数据


class ThreadRead(threading.Thread):
    '''这个进程负责读取数据'''
    def __init__(self, name, queue):
        threading.Thread.__init__(self)
        self.name = name
        self.data = queue

    def run(self):
        for i in range(5):
            time.sleep(1)  # 等待数据写入，然后再读取
            print('%s read %s' % (self.getName(), self.data.get()))


if __name__ == '__main__':
    q = queue.Queue()  # 创建队列
    tw = ThreadWrite('w', q)
    tr = ThreadRead('r', q)
    tw.start()
    tr.start()
    tw.join()
    tr.join()
