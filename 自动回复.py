import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import os
from itchat.content import *

@itchat.msg_register(TEXT, isFriendChat=True)   #这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
def simple_reply(msg):
    #这个是向发送者发送消息
    print(msg['FromUserName'])
    if msg['FromUserName'] == '李靖':
        itchat.send_msg(msg['Text'],toUserName=msg['FromUserName'])
    # return "T reveived: %s" % msg["Text"]     #返回的给对方的消息，msg["Text"]表示消息的内容
