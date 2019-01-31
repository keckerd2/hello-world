import urllib.parse
import urllib.request

url = 'http://www.renren.com/77425/profile'
# 构建表头，假装用户行为
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie':'anonymid=iyjdbvnp2vdlek; __utma=10481322.951420450.1501735868.1501735868.1501735868.1; _r01_=1; _de=8638DC82B6DF1573667759B300E60630; depovince=ZGQT; jebecookies=251e9f35-0f01-44e2-aa80-9490bf866398|||||; JSESSIONID=abc1tAWS3NEgu9oGFh_Hw; p=0a90db3c3d567d3512e9c6f4759ef7bf5; first_login_flag=1; ln_uact=13811845106; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20100524/2015/h_main_Ry0T_454800020de02f74.jpg; t=e0782002c45474075677a62ef55095d15; societyguester=e0782002c45474075677a62ef55095d15; id=77425; xnsid=81df634a; ver=7.0; loginfrom=null; wp_fold=0',
}
# 构建请求对象
request = urllib.request.Request(url, headers = headers)

# 发送请求
response = urllib.request.urlopen(request)
with open('renren.html','wb') as fp:
    fp.write(response.read())
