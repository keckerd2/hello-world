import re

########################搜索#####################
string = '<p><div><span>猪八戒</span></div></p>'
pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')
# 上面\1 \2是第1个和第2个括号里的内容
# \w+不能匹配换行

string = '<div>猪八戒</div></div></div></div></div>'
pattern = re.compile(r'<div>.*</div>') #贪婪模式
pattern = re.compile(r'<div>.*?</div>')#加?为不贪婪模式

ret = pattern.search(string)
# print(ret)

string = '''hello word
my name is 
my world is
fun haha'''
pattern = re.compile(r'^my', re.M) #re.M为多行模式，不加就搜不到
ret = pattern.match(string)     #从开始找第一个
ret = pattern.search(string)    #从任意位置找第一个
ret = pattern.findall(string)   #找所有
# print(ret)

string2 = """<div>
我是一个冰
来自老百姓
</div>"""
pattern = re.compile(r'<div>(.*?)</div>', re.S)    #re.S为单行模式，此模式中.可以匹配换行符
                                                    #用括号就只要里面的了，不要<div>
ret = pattern.findall(string2)
# print(ret)

#re.I忽略大小写

#############替换#################################################
# re.sub(正则表达式，替换内容，字符串)
string = 'I love you ,you love her ,oh'
pattern = re.compile(r'love')
ret = re.sub(pattern,'hate',string)
# ret = pattern.sub('hate',string ) 两种写法都行
# print(ret)

#########身高+10的我的写法
def fn(ret):
    return str(int(ret[0])+10)
string = '我要长到180身高'
pattern = re.compile(r'(\d+)')
ret = pattern.findall(string)
ret2 = re.sub(pattern,fn(ret),string)

# print(ret2)

#########身高+10的专业写法
def fn(ret):
    return str(int(ret.group(0))+10) #group（0）在正则表达式中用于获取分段截获的字符串
string = '我要长到150身高'
pattern = re.compile(r'(\d+)')
ret = pattern.sub(fn,string )

print(ret)
