import itchat
from itchat.content import TEXT
from itchat.content import *
import sys
import time
import re
import os

msg_information = {}

# @itchat.msg_register([TEXT, PICTURE, FRIENDS, CARD, MAP, SHARING, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True, isGroupChat=True, isMpChat=True)
# def judge_rp(msg):
#     print(msg)

# def send_message(message):
#     # nickname = input('please input your firends\' nickname : ' )
#     #   想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
#     # users = itchat.search_friends(name=nickname)
#     users = itchat.search_friends(name='d2')   # 使用备注名来查找实际用户名
#     #获取好友全部信息,返回一个列表,列表内是一个字典
#     print(users)
#     #获取`UserName`,用于发送消息
#     userName = users[0]['UserName']
#     itchat.send(message,toUserName = userName)
#     print('succeed')
#
#
#     # itchat.auto_login(enableCmdQR=True)
@itchat.msg_register(NOTE,isGroupChat=True)#监听群内红包消息
def receive_red_packet(msg):
    print(msg['Content'])
    if  msg['Content'] == '收到红包，请在手机上查看':
        groups  = itchat.get_chatrooms(update=True)
        # users = itchat.search_chatrooms(name=u'Happy一家人')#把红包消息通知给这个群
        # userName = users[0]['UserName']#获取这个群的唯一标示
        for g in groups:
            if msg['FromUserName'] == g['UserName']:#根据群消息的FromUserName匹配是哪个群
                group_name = g['NickName']
        msgbody = '红包！' + group_name
        # msgbody = msg['User']['NickName'] + ' 红包！'
        print(msgbody)
        # users = itchat.search_friends(name='李靖')
        # userName = users[0]['UserName']
        # itchat.send(msgbody,toUserName = userName)
        user = itchat.search_friends(name='李靖')[0]
        user.send(msgbody)
        itchat.send(msgbody, toUserName='filehelper')

itchat.auto_login(hotReload=True)  # 首次扫描登录后后续自动登录

# itchat.send('测试发消息给自己')
# @itchat.msg_register(TEXT)   #这里的TEXT表示如果有人发送文本消息，那么就会调用下面的方法
# def simple_reply(msg):
#     #这个是向发送者发送消息
#     # itchat.send_msg('已经收到了文本消息，消息内容为%s'%msg['Text'],toUserName=msg['FromUserName'])
#     # return "T reveived: %s" % msg["Text"]     #返回的给对方的消息，msg["Text"]表示消息的内容
#     print(msg)
itchat.run()
