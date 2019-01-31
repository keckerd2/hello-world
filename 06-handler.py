import urllib.parse
import urllib.request
url = 'https://www.baidu.com/'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

# 创建handler
handler = urllib.request.HTTPHandler()
# 通过handler创建opener,opener是一个对象，需要发送请求的时候直接使用opener里的方法
opener = urllib.request.build_opener(handler)

# 构建请求对象
request = urllib.request.Request(url, headers = headers)

# 发送请求
response = opener.open(request)
print(response.read().decode())
