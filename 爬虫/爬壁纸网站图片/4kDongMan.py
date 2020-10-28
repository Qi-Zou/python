# 需要的包
import urllib.request
import re
import os
import urllib
import requests
import time
import signal
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures._base import as_completed


    # 自定义超时异常
class TimeoutError(Exception):
    def __init__(self, msg):
        super(TimeoutError, self).__init__()
        self.msg = msg


def theme(dir_name , describe):
    print(describe)
    # 处理分页，每一页都按照下面的流程进行即可
    # 先试试看下面的流程是否可以走通
    # 可以走通，我们继续做分页爬取
    main_index_html = 'http://pic.netbian.com/'+dir_name+'/'   # 这是首页地址
    index_html = main_index_html    # 这是当前爬取的页面地址
    for index in range(1,201):  # 从第一页爬到最大页码（注意，这个是左包含）
        # 由于首页没有 index_x.html 这样的，因此直接使用首页地址即可，其他的页码需要作处理
        if(index != 1):
            index_html = main_index_html + "index_" + str(index) + ".html"
        print("index_html = " + index_html)
        try:
            page(index_html , dir_name)
        except:
            pass

def handler(signum, frame):
    raise TimeoutError("run func timeout")

# 每一页的操作
def page(index_html , dir_name):
    main_addr = 'http://pic.netbian.com/'
    html_data = get_html(index_html)
    pat = '/tupian/(.*?).html'
    # 这里获取出来的是图片跳转的地址上的数字
    xiao_tu_pian = get_addr(pat , html_data)
    for xtp in xiao_tu_pian:
        xtp_addr = main_addr + '/tupian/' + xtp + ".html"
        print('xtp_addr = ' + xtp_addr)
        # 根据正则 匹配出图片所在页面中，图片的真实地址
        da_tu_pian = get_addr('/uploads/allimg/(.*?).jpg' , get_html(xtp_addr))
        # 由于匹配出来的图片会有很多，通过查看，可以发现我们需要的图片是在第一章，因此我们只需要取第一个的地址即可
        dtp_addr = main_addr + '/uploads/allimg/' + da_tu_pian[0] + '.jpg'
        print('dtp_addr = ' + dtp_addr)
        # 由于我们匹配出来的地址会有一个 '/' 因此，我们只需要取后面的数字作为文件名即可 ， 需要分割
        save_addr = '/home/yefan/Work/pythonWorkSpace/Spider/'+dir_name+'/' + da_tu_pian[0].split("/")[1] + '.jpg'
        print("save_addr = " + save_addr)
        # 最后一步， 开始下载     
        download_img(dtp_addr , save_addr)
          
# 根据正则匹配需要查找的图片路径
def get_addr(pat , html_data):
    result = re.compile(pat).findall(html_data)
    return result
# 获取网页内容
def get_html(url):
    page_data = urllib.request.urlopen(url)
    html_a = page_data.read()
    return html_a.decode('cp936')


def time_out(interval, callback):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("run func timeout")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)       # interval秒后向进程发送SIGALRM信号
                result = func(*args, **kwargs)
                signal.alarm(0)              # 函数在规定时间执行完后关闭alarm闹钟
                return result
            except TimeoutError as e:
                callback(e)
        return wrapper
    return decorator

def timeout_callback(e):
    print(e.msg)

# 下载图片
# @time_out(2, timeout_callback)
def download_img(img_addr , save_addr):
    urllib.request.urlretrieve(img_addr , save_addr)


def main():
    theme_name = ['4kmeishi','4kzongjiao','4kbeijing']
    executor = ThreadPoolExecutor(max_workers=len(theme_name))
    future_list =list()
    for dir_name in theme_name:
        future_list.append(executor.submit(theme, dir_name , dir_name + "下载中："))
    for future in future_list:
        future.result()

# async
        # _thread.start_new_thread( theme, (dir_name, "线程【"+dir_name+"】下载中：\n") )
    # _thread.start_new_thread( theme, (theme_name[1], "线程【"+theme_name[1]+"】下载中：\n") )
    # _thread.start_new_thread( theme, (theme_name[2], "线程【"+theme_name[2]+"】下载中：\n") )



if __name__ == "__main__":
    main()




