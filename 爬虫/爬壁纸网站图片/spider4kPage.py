import urllib.request
import re
import os
import urllib
import requests

# 匹配分页
# 匹配小图片路径
# 匹配正常图片路径
# 下载图片

def main():
    main_index_html = 'http://pic.netbian.com/4kdongman/'
    index_html = main_index_html
    for index in range(108,115):
        if(index != 1):
            index_html = main_index_html + "index_"+str(index)+".html"
        print(index_html)
        page(index_html)

# 根据页码下载
def page(index_html):
    main_addr = 'http://pic.netbian.com/'
    html_data = get_html(index_html)
    pat = '/tupian/(.*?).html'
    xiao_tu_pian = get_addr(pat , html_data)
    for xtp in xiao_tu_pian:
        xtp_addr = main_addr + '/tupian/'+xtp+'.html'
        print(xtp_addr)
        da_tu_pian = get_addr('/uploads/allimg/(.*?).jpg',get_html(xtp_addr))
        dtp_addr = main_addr + '/uploads/allimg/'+da_tu_pian[0]+'.jpg'
        print(dtp_addr)
        save_addr = '/home/yefan/Work/pythonWorkSpace/Spider/img/'+da_tu_pian[0].split("/")[1]+'.jpg'
        print(save_addr)
        download_img(dtp_addr , save_addr)

# 根据匹配规则查找所有的路径
def get_addr(pat , html_data):
    result = re.compile(pat).findall(html_data)
    return result

# 获取网站内容
def get_html(url):
    page = urllib.request.urlopen(url)
    html_a = page.read()
    return html_a.decode('cp936')

# 下载图片
def download_img(img_url , save_addr):
    # urllib.request.urlretrieve(img_url, save_addr) #下载图片
    r = requests.get(img_url)
    with open(save_addr, "wb") as code:
        code.write(r.content)


if __name__ == "__main__":
    main()