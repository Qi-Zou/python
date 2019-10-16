#我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self , threadID , name , delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self) -> None:
        print("开始线程：" + self.name)
        print_thread(self.name , self.delay , 5)
        print("退出线程:"+self.name)

def print_thread(threadName , delay , counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{}:{}".format(threadName , time.ctime(time.time())))
        counter -= 1
        pass

thread1 = myThread(1 , "Thread-1" , 2)
thread2 = myThread(2 , "Thread-2" , 4)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("退出主线程")

