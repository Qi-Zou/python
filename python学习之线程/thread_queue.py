# 线程优先级队列
import queue
import threading
import time

exitFlag = 0
queueLock = threading.Lock()
workQueue = queue.Queue(10)

class myThread(threading.Thread):
    def __init__(self , threadID , name , q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self) -> None:
        print("开启线程:" + self.name)
        process_data(self.name , self.q)
        print("退出线程：" + self.name)
def process_data(threadName , q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("{}:{}".format(threadName , data))
        else:
            queueLock.release()
        time.sleep(2)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
threads = []
threadID = 1

for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空,再去补充队列的东西　，　这里将是死循环
while 1:
    if workQueue.empty():
        queueLock.acquire()
        for word in nameList:
            workQueue.put(word)
        queueLock.release()
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")