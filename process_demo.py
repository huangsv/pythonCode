import multiprocessing
import time


class SubProcess(multiprocessing.Process):
    def __init__(self, arg, title='p'):
        # 调用父类的初始化方法
        multiprocessing.Process.__init__(self)
        self.arg = arg
        if title:
            self.title = title

    def run(self):
        '''进程调用执行的方法体为 run'''
        for i in range(50):
            print('%s 进程 %s ' % (self.title, self.arg))
            time.sleep(1)
            
            
if __name__ == '__main__':
    # 直接实例化被其继承的类
    p1 = SubProcess(arg=1)
    p2 = SubProcess(arg=2, title='p2')
    p1.start()
    p2.start()
    p1.join()
    p2.join()
