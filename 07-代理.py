import urllib.parse
import urllib.request

def test_proxy(ip_port, choice='http'):
    proxies = None
    # 这个网站可以返回你公网下的IP，如果你加代理请求后，返回的就是你代理的IP（这样做是防止你虽然用的是代理IP，但实际是用你自己的公网IP访问的请求）
    tar_url = "http://icanhazip.com/"
    user_agent = self.get_user_agent()
    headers = {'User-Agent': user_agent}
    if choice == 'http':
        proxies = {
            "http": "http://"+ip_port,
        }

    elif choice == 'https':
        proxies = {
            "https": "https://" + ip_port,
        }
    try:
        thisIP = "".join(ip_port.split(":")[0:1])
        res = requests.get(tar_url, proxies=proxies, headers=headers, timeout=8)
        proxyIP = res.text.strip()
        if proxyIP == thisIP:
            return proxyIP
        else:
            return False
    except:
        return False

# 创建代理handler，27.29.44.224：9999
handler = urllib.request.ProxyHandler({'http':'116.209.55.234:9999'})
print(test_proxy('116.209.55.234:9999'))
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
print(response.read().decode())
with open('ip.html','wb') as fp:
    fp.write(response.read())

