import _thread
import time

def print_thread(threadName , dalay):
    '''
    为线程定义一个函数
    :param threadName:
    :param dalay:
    :return:
    '''
    count = 0
    while count < 5 :
        time.sleep(dalay)
        print("{}:{}".format(threadName , time.ctime(time.time())))
        count += 1

def create_thread():
    '''
    创建线程
    :return:
    '''
    try:
        _thread.start_new_thread(print_thread, ("Thread_1", 2,))
        _thread.start_new_thread(print_thread, ("Thread_2", 4,))
    except:
        print("Error : 无法启动线程")


# 开始
print("开始")
create_thread()

time.sleep(20)
print("结束")
