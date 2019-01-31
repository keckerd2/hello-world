import urllib.parse
import urllib.request

# POST地址
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

# 构建表单
form_data ={
    'cname':'北京',
    'pid':'',
    'pageIndex':'2',
    'pageSize':'10',
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
response = urllib.request.urlopen(request, data = form_data)

print(response.read().decode())
