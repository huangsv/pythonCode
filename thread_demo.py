import threading, time


# 创建一个子类MyThread子类，继承threading.Thread线程类
class MyThread(threading.Thread):
    # 调用对象 start() 方法时，程序会自动调用run()方法
    def run(self):
        for i in range(5):
           time.sleep(1)
           msg = '子线程' + self.name + '执行'
           print(msg)


if __name__ == '__main__':
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
