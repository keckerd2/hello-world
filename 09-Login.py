import urllib.parse
import urllib.request
import http.cookiejar

# 创建COOKIEJAR对象
cj = http.cookiejar.CookieJar()
# 通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
# 通过handler创建opener
opener = urllib.request.build_opener(handler)

url = 'https://www.jisilu.cn/account/ajax/login_process/'
# 构建表单
form_data ={
    'return_url' :	'https://www.jisilu.cn/',
    'user_name' :	'kecker',
    'password' :	'wodeshengri',
    'net_auto_login' :	'1',
    '_post_type' :	'ajax',
}

# 构建表头，假装用户行为
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url, headers = headers)
# 处理post表单数据
form_data = urllib.parse.urlencode(form_data).encode()
# 发送请求
response = opener.open(request, data = form_data)
# 登录收到的返回是一个JSON数据
# print(response.read().decode())

# 登录后访问数据
get_url = 'https://www.jisilu.cn/data/mine/'
request = urllib.request.Request(get_url, headers = headers)
response = opener.open(request, data = form_data)
print(response.read().decode())

