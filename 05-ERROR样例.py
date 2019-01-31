import urllib.parse
import urllib.request
import urllib.error

# url = 'http://www.maodan.com/'
url = 'http://blog.sina.com.cn/s/articlelist_14330984_0_1.html'

try:
    response = urllib.request.urlopen(url)
    print(response)

except urllib.error.HTTPError as e:
    print(e)
    print(e.code)
except urllib.error.URLError as e:
    print(e)
