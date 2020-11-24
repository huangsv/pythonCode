import threading, time


def task():
    for x in range(5):
        print('线程(%s) 输出' % threading.current_thread().name)
        time.sleep(0.5)
        print()
        
        
if __name__ == '__main__':
    # 使用列表推导式创建 4 个线程
    ts = [threading.Thread(target=task) for i in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
