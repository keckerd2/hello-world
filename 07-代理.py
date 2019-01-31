import urllib.parse
import urllib.request

# 创建代理handler，27.29.44.224：9999
handler = urllib.request.ProxyHandler({'http':'27.29.44.224:9999'})

# 通过handler创建opener
opener = urllib.request.build_opener(handler)

#HTTPS的不成功
# url = 'https://www.baidu.com/s?wd=ip&ie=UTF-8'
url = 'http://www.baidu.com/s?wd=ip&ie=UTF-8'


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url, headers = headers)
# 发送请求
response = opener.open(request)
# print(response.read().decode())
with open('ip.html','wb') as fp:
    fp.write(response.read())

