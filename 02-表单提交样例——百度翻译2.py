import urllib.parse
import urllib.request

# POST地址
url = 'https://fanyi.baidu.com/v2transapi'
word = 'wolf'
# 构建表单
form_data ={
    'from':'en',
    'to':'zh',
    'query':word,
    'transtype':'realtime',
    'simple_means_flag':'3',
    'sign':'275695.55262',
    'token':'0e88304a43e6bff60388085ae2671df5',
#     最后两个参数是根据要查的单词用JS算出来的值，不同单词会不一样，需要破解
}
# 构建表头，假装用户行为
headers = {
    # 'Accept':'*/*',
    # 不要压缩
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7',
    # 'Connection':'keep-alive',
    # 'Content-Length':'120',  #长度也不要
    # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BIDUPSID=B14096A622DFA3F04631E7BCEA38F8B8; PSTM=1483836710; __cfduid=d452a3ff98982d595a12b82a8362e37c11532498531; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-%3A; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BAIDUID=625F15CD147500E77FE31463BAD3B580:FG=1; BDUSS=mMxWkxhaG1YOW5jMzhzQnZ-a0w5TUFuMGsxQTBlRUxmcnNIMTBUVXpha2U1bWRjQVFBQUFBJCQAAAAAAAAAAAEAAACOVYYAa2Vja2VyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB5ZQFweWUBcW; locale=zh; delPer=0; PSINO=1; H_PS_PSSID=1421_21083_28329_28132_26350_28413; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1546504990,1548060397,1548213402; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1548213402',
    'Host':'fanyi.baidu.com',
    'Origin':'https://fanyi.baidu.com',
    'Referer':'https://fanyi.baidu.com/',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
# 构建请求对象
request = urllib.request.Request(url, headers = headers)
# 处理post表单数据
form_data = urllib.parse.urlencode(form_data).encode()
# 发送请求
response = urllib.request.urlopen(request, data = form_data)

print(response.read().decode())
