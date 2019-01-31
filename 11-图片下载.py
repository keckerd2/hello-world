import urllib.parse
import urllib.request
import re
import os

def handle_request(url,page):
    url += page
    url += '/'
    headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
    # 构建请求对象
    return urllib.request.Request(url, headers = headers)

def download_image(content):
    # pattern = re.compile(r'<img src="//(.*\.jpeg)"',re.I)
    pattern = re.compile(r'<div class="thumb">.*?<img src="//(.*?)".*?</div>',re.S)
    ret = pattern.findall(content)
    for pic_url in ret:
        pic_url = 'https://'+pic_url
         # 创建文件夹
        dir_name = 'qiutu'
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        # 图片名
        filename = pic_url.split('/')[-1]
        filepath = dir_name + '/' + filename
        urllib.request.urlretrieve(pic_url, filepath)

def main():


    url = 'https://www.qiushibaike.com/pic/page/'
    end_page = 2
    for page in range(1,end_page+1):
        print('第%d页开始下载---------' % page)
        #生成请求对象
        request = handle_request(url,str(page))
        # 发送请求
        content = urllib.request.urlopen(request).read().decode()
        download_image(content)
        print('第%d页下载结束---------' % page)






if __name__ == '__main__':
    main()
