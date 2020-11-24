import threading


number = 10


def task():
    global number  # 使用全局变量
    mutex.acquire()  # 上锁
    number -= 1
    print('数据使用完成，准备解锁，数据为 %s' % number)
    mutex.release()  # 释放锁


if __name__ == '__main__':
    mutex = threading.Lock()  # 创建一把锁
    ts = [threading.Thread(target=task) for i in range(10)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
