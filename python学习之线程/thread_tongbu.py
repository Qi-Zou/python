import threading
import time


threadLock = threading.Lock()
threads = []

class myThread(threading.Thread):
    def __init__(self , threadID, name , dalay):
        threading.Thread.__init__(self)
        self.threadId = threadID
        self.name = name
        self.dalay = dalay

    def run(self) -> None:
        print("开启线程　：" +self.name)
        # 获得锁　，　用户线程同步
        threadLock.acquire()
        print_thread(self.name , self.dalay , 5)
        # 释放锁
        threadLock.release()

def print_thread(threadName , delay , counter):
    while counter:
        time.sleep(delay)
        print("{}:{}".format(threadName , time.ctime(time.time())))
        counter -= 1

thread1 = myThread(1 , "Thread - 1" , 1)
thread2 = myThread(2 , "Thread - 2" , 2)

thread1.start()
thread2.start()
threads.append(thread1)
threads.append(thread2)


for th in threads:
    th.join()

print("退出主线程")


