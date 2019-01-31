import urllib.parse
import urllib.request

# POST地址
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=20&limit=20'
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='
page = 1
number = 2

data = {
    'start' : page*20-20 ,
    'limit' : number,
}
# 字典转化为GET的参数
query_string = urllib.parse.urlencode(data)
# 构建表头，假装用户行为
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url+query_string, headers = headers)

# 发送请求
response = urllib.request.urlopen(request)

print(response.read().decode())
